#
# PySNMP MIB module CISCO-WAN-ATM-PARTY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-ATM-PARTY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:20:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, iso, TimeTicks, Bits, Counter32, Counter64, NotificationType, ObjectIdentity, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "TimeTicks", "Bits", "Counter32", "Counter64", "NotificationType", "ObjectIdentity", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "Unsigned32")
RowStatus, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TruthValue")
ciscoWanAtmPartyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 99998))
ciscoWanAtmPartyMIB.setRevisions(('2002-06-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanAtmPartyMIB.setRevisionsDescriptions(('Initial version of the MIB',))
if mibBuilder.loadTexts: ciscoWanAtmPartyMIB.setLastUpdated('200206170000Z')
if mibBuilder.loadTexts: ciscoWanAtmPartyMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanAtmPartyMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com ')
if mibBuilder.loadTexts: ciscoWanAtmPartyMIB.setDescription("A management station can use this MIB to provision, manage or delete one or more 'parties' on an ATM point-to-multipoint Soft PVCC(SPVC) connection. The user must add a root endpoint to the managed system before proceed to add one or more 'parties' to the root. The provision and management of a 'root' endpoint is beyond the scope of this MIB. Please refer to CISCO-WAN-ATM-CONN-MIB.my for the provisioning and management of a 'root' endpoint. This MIB is based on 'ITU-T recommendation Q.2971 (10/95) BROADBAND INTEGRATED SERVICES DIGITAL NETWORK (B-ISDN) - DIGITAL SUBSCRIBER SIGNALLING SYSTEM No. 2 (DSS 2) - USER-NETWORK INTERFACE LAYER 3 SPECIFICATION FOR POINT- TO-MULTIPOINT CALL/CONNECTION CONTROL")
ciscoWanAtmPartyMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 0))
ciscoWanAtmPartyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1))
cwapConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1))
ciscoWanAtmPartyMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 2))
class WanPartyAdminStatus(TextualConvention, Integer32):
    description = "Defines 'administrative status' of a 'party'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class WanPartyOperStatus(TextualConvention, Integer32):
    description = "Defines 'operational status' of a 'party'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ok", 1), ("fail", 2))

class WanNsapAtmAddress(TextualConvention, OctetString):
    description = 'ATM address used by the managed system. The only address type presently supported is ATM Network Service Access Point (NSAP) addresses (20 octets).'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(20, 20)
    fixedLength = 20

cwapConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1), )
if mibBuilder.loadTexts: cwapConfigTable.setStatus('current')
if mibBuilder.loadTexts: cwapConfigTable.setDescription("This table contains mandatory 'party' configuration for all ATM point-to-multipoint Soft Permanent Virtual Channel Connections (SPVC). ")
cwapConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WAN-ATM-PARTY-MIB", "cwapRootVpi"), (0, "CISCO-WAN-ATM-PARTY-MIB", "cwapRootVci"), (0, "CISCO-WAN-ATM-PARTY-MIB", "cwapReference"))
if mibBuilder.loadTexts: cwapConfigEntry.setStatus('current')
if mibBuilder.loadTexts: cwapConfigEntry.setDescription("An entry in the 'cwapConfigTable'. Each entry corresponds to one party of a point-to-multipoint connection. (1) To add an entry, the management application must first provision a 'root' endpoint. (2) While adding an entry, the variables 'cwapNSAPAddress', 'cwapVpi' and 'cwapVci' are mandatory. The 'cwapNSAPAddress', 'csapVpi' and 'cwapVci' are not required to be unique. (3) The row creation will fail if the root endpoint does not exist. (4) The following management operations are permitted on a row when the 'cwapRowStatus' is 'active': a) row deletion. b) toggling of the administrative status of a 'party' via the 'cwapAdminStatus' object. c) triggering a reroute via the 'cwapReroute' object. (5) The table index 'ifIndex' refers to that of the root. The 'ifIndex' identifies an ATM Virtual Interface ('ifType' atmVirtual(149)). ")
cwapRootVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095)))
if mibBuilder.loadTexts: cwapRootVpi.setStatus('current')
if mibBuilder.loadTexts: cwapRootVpi.setDescription('This object identifies the Virtual Path Identifier(VPI) of the root endpoint this party is associated with.')
cwapRootVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: cwapRootVci.setStatus('current')
if mibBuilder.loadTexts: cwapRootVci.setDescription('This object identifies the Virtual Channel Identifier (VCI) of the root endpoint this party is associated with.')
cwapReference = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: cwapReference.setStatus('current')
if mibBuilder.loadTexts: cwapReference.setDescription('An arbitrary integer which serves to distinguish between the multiple parties attached to a root of a point-to-multipoint SPVC.')
cwapNSAPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 4), WanNsapAtmAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapNSAPAddress.setStatus('current')
if mibBuilder.loadTexts: cwapNSAPAddress.setDescription('The ATM NSAP address of this party.')
cwapVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapVpi.setStatus('current')
if mibBuilder.loadTexts: cwapVpi.setDescription('The VPI value of this party.')
cwapVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapVci.setStatus('current')
if mibBuilder.loadTexts: cwapVci.setDescription('The VCI value of this party.')
cwapReroute = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapReroute.setStatus('current')
if mibBuilder.loadTexts: cwapReroute.setDescription("The management station uses this object to trigger the re-routing of the party. * Rerouting takes effect, when this object is set to true(1). When set to false(2), no action is taken. * The value 'false' will always be returned on snmp query to this variable. * During reroute operation, the 'cwapOperStatus' will contain the value 'fail'. Upon successful completion of reroute, the 'cwapOperStatus' will change to the value 'ok'. If the reroute operation failed, the 'cwapOperStatus' will stay in 'fail'. The management station should query the 'cwapOperStatus' to decide if a reroute request is successful or not.")
cwapAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 8), WanPartyAdminStatus().clone('up')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapAdminStatus.setStatus('current')
if mibBuilder.loadTexts: cwapAdminStatus.setDescription("The 'administrative status' of this party. ")
cwapOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 9), WanPartyOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwapOperStatus.setStatus('current')
if mibBuilder.loadTexts: cwapOperStatus.setDescription("The 'operational status' of this party.")
cwapIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwapIdentifier.setStatus('current')
if mibBuilder.loadTexts: cwapIdentifier.setDescription('An arbitrary integer which serves to distinguish all parties on a node. This value is assigned by the managed system when a party is added. The use of this variable is implementation specific.')
cwapUploadCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwapUploadCounter.setStatus('current')
if mibBuilder.loadTexts: cwapUploadCounter.setDescription('This counter is used by the management station to determine if a party had been modified and requires further action from management station. The use of this variable is implementation specific. This functionality is conventionally achieved by time stamping using a time-of-day clock. However, in switches where time-of-day clock is not available, the following scheme is used: The upload counter is incremented, when: * assignment of a party to a cwapIdentifier. This happens when a party is added and assigned this cwapIdentifier. * de-assignment of connection from a cwapIdentifier. This happens when a connection is deleted. * When there is a status change done to this party.')
cwapRootPhysicalId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwapRootPhysicalId.setStatus('current')
if mibBuilder.loadTexts: cwapRootPhysicalId.setDescription('This object contains physical description of the physical interface the root resides. The presentation of this object is implementation specific.')
cwapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapRowStatus.setStatus('current')
if mibBuilder.loadTexts: cwapRowStatus.setDescription("This object is used to create, modify or delete an entry in the ciscoWanAtmPartyTable. * A row may be created using the 'CreateAndGo' option. When the row is successfully created, the RowStatus would be set to 'active' by the agent. * A row may be deleted by setting the RowStatus to 'destroy'. ")
ciscoWanAtmPartyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 2, 1))
ciscoWanAtmPartyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 2, 2))
ciscoWanAtmPartyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 99998, 2, 1, 1)).setObjects(("CISCO-WAN-ATM-PARTY-MIB", "ciscoWanAtmPartyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmPartyMIBCompliance = ciscoWanAtmPartyMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoWanAtmPartyMIBCompliance.setDescription('The compliance statement for SNMPv2 entities which implement one or more parties of an ATM point-to- multi-point connection.')
ciscoWanAtmPartyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 99998, 2, 2, 2)).setObjects(("CISCO-WAN-ATM-PARTY-MIB", "cwapNSAPAddress"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapVpi"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapVci"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapAdminStatus"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapOperStatus"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapReroute"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapIdentifier"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapUploadCounter"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapRootPhysicalId"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmPartyGroup = ciscoWanAtmPartyGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoWanAtmPartyGroup.setDescription("This group contains the information of a 'party' per each SPVC point-to-multipoint connection.")
mibBuilder.exportSymbols("CISCO-WAN-ATM-PARTY-MIB", ciscoWanAtmPartyMIBGroups=ciscoWanAtmPartyMIBGroups, ciscoWanAtmPartyMIBObjects=ciscoWanAtmPartyMIBObjects, cwapRowStatus=cwapRowStatus, cwapReference=cwapReference, cwapRootVci=cwapRootVci, ciscoWanAtmPartyMIBConform=ciscoWanAtmPartyMIBConform, cwapRootVpi=cwapRootVpi, ciscoWanAtmPartyMIB=ciscoWanAtmPartyMIB, cwapConfigTable=cwapConfigTable, WanPartyAdminStatus=WanPartyAdminStatus, cwapConfig=cwapConfig, cwapRootPhysicalId=cwapRootPhysicalId, ciscoWanAtmPartyMIBNotifs=ciscoWanAtmPartyMIBNotifs, cwapVci=cwapVci, ciscoWanAtmPartyMIBCompliances=ciscoWanAtmPartyMIBCompliances, cwapOperStatus=cwapOperStatus, cwapUploadCounter=cwapUploadCounter, cwapNSAPAddress=cwapNSAPAddress, cwapReroute=cwapReroute, cwapVpi=cwapVpi, ciscoWanAtmPartyGroup=ciscoWanAtmPartyGroup, PYSNMP_MODULE_ID=ciscoWanAtmPartyMIB, WanNsapAtmAddress=WanNsapAtmAddress, cwapIdentifier=cwapIdentifier, cwapAdminStatus=cwapAdminStatus, ciscoWanAtmPartyMIBCompliance=ciscoWanAtmPartyMIBCompliance, WanPartyOperStatus=WanPartyOperStatus, cwapConfigEntry=cwapConfigEntry)
