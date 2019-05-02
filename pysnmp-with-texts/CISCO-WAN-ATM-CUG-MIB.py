#
# PySNMP MIB module CISCO-WAN-ATM-CUG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-ATM-CUG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:20:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
AtmAddr, = mibBuilder.importSymbols("ATM-TC-MIB", "AtmAddr")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, ModuleIdentity, NotificationType, Bits, MibIdentifier, Counter64, iso, Integer32, Unsigned32, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Bits", "MibIdentifier", "Counter64", "iso", "Integer32", "Unsigned32", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
ciscoWanAtmCugMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 99999))
ciscoWanAtmCugMIB.setRevisions(('2002-03-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanAtmCugMIB.setRevisionsDescriptions(('Initial version of the MIB.',))
if mibBuilder.loadTexts: ciscoWanAtmCugMIB.setLastUpdated('200203220000Z')
if mibBuilder.loadTexts: ciscoWanAtmCugMIB.setOrganization('Cisco System Inc.')
if mibBuilder.loadTexts: ciscoWanAtmCugMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive, San Jose CA 95134-1706. USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanAtmCugMIB.setDescription("This MIB module is intended for the management of 'Closed User Group(CUG)' in Cisco ATM switches. This MIB definition is based upon 'Closed User Group' recommended by International Telecommunication Union(ITU). The CUG supplementary service enables users to form groups, to and from which access is restricted. A specific user may be member of one or more closed user groups. Members of a specific closed user group can communicate among themselves but not, in general, with users outside the group. Specific CUG members can have additional capabilities that allow them to originate calls to destinations outside the group, and/or to receive calls from outside the group. Specific CUG members can have additional restrictions that prevent them from originating calls to other members of the CUG, or from receiving calls from other members of the CUG. ITU-T Q.2955.1 Stage 3 description for community of interest supplementary services using B-ISDN Digital Subscriber Signalling System No.2(DSS 2): Closed User Group(CUG).")
cwaCugMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 0))
cwaCugMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1))
cwaCug = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1))
cwaAddressCug = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2))
class CiscoAtmAddressType(TextualConvention, Integer32):
    description = 'The type of an ATM Address. The value e164(3) indicates the address format is that of ITU-T defined address format. The value nsap(8) indicates the address format is that of ATM private network address or ATM end-point identifiers. The CiscoAtmAddressType textual convention SHOULD NOT be subtyped in object type definitions to support future extensions. It MAY be subtyped in compliance statements in order to require only a subset of these address types for a compliant implementation. Note that the enumerated values of this TC are aligned with AddressFamilyNumbers from IANA-ADDRESS-FAMILY-NUMBERS-MIB.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 8))
    namedValues = NamedValues(("e164", 3), ("nsap", 8))

class CiscoAtmAddressLength(TextualConvention, Integer32):
    description = 'The length (in bits) of an ATM Address.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 160)

class CiscoAtmInterlockCode(TextualConvention, OctetString):
    reference = 'ATM Forum, Closed User Group, Section 3'
    description = "A Closed User Group(CUG) Interlock Code. Each 'Interlock Code' uniquely identifies a Closed User Group in the network. This is a 'PNNI Interlock Code', it contains a 20-octet ATM End Station Address(AESA) and a 4-octet Suffix. "
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(24, 24)
    fixedLength = 24

cwaCugTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1), )
if mibBuilder.loadTexts: cwaCugTable.setStatus('current')
if mibBuilder.loadTexts: cwaCugTable.setDescription('This table contains a sequence of CUGs for each ATM address.')
cwaCugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-WAN-ATM-CUG-MIB", "cwaAtmAddress"), (0, "CISCO-WAN-ATM-CUG-MIB", "cwaAddressLength"), (0, "CISCO-WAN-ATM-CUG-MIB", "cwaCugIndex"))
if mibBuilder.loadTexts: cwaCugEntry.setStatus('current')
if mibBuilder.loadTexts: cwaCugEntry.setDescription('The entry represents one CUG for an ATM address.')
cwaAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 1), AtmAddr())
if mibBuilder.loadTexts: cwaAtmAddress.setStatus('current')
if mibBuilder.loadTexts: cwaAtmAddress.setDescription('A provisioned ATM address on the managed system.')
cwaAddressLength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 2), CiscoAtmAddressLength())
if mibBuilder.loadTexts: cwaAddressLength.setStatus('current')
if mibBuilder.loadTexts: cwaAddressLength.setDescription("This is the length (in bits) of the 'cwtAtmAddress'. ")
cwaCugIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: cwaCugIndex.setReference('ITU-T Specification Q.2955.1 section 1.3.3')
if mibBuilder.loadTexts: cwaCugIndex.setStatus('current')
if mibBuilder.loadTexts: cwaCugIndex.setDescription("The CUG index is a parameter used by the calling user to select a particular CUG when originating a call. The index is also used by the network to indicate to the called user the CUG from which an incoming call has originated. This index has only local significance. Each 'cwaCugIndex' assigned to an ATM address must be unique for this ATM address. For each 'cwaCugIndex' must have one corresponding cwaInterLockCode assigned.")
cwaAddressPlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 4), CiscoAtmAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaAddressPlan.setStatus('current')
if mibBuilder.loadTexts: cwaAddressPlan.setDescription('This is the type of the ATM address associated with this entry.')
cwaInterlockCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 5), CiscoAtmInterlockCode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaInterlockCode.setReference('ATM Forum, Closed User Group, Section 3')
if mibBuilder.loadTexts: cwaInterlockCode.setStatus('current')
if mibBuilder.loadTexts: cwaInterlockCode.setDescription("This is the 'Closed User Group(CUG) Interlock Code' associated with this entry.")
cwaCallsBarred = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("incoming", 2), ("outgoing", 3))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaCallsBarred.setReference('ITU-T Specification Q.2955.1 Sections 1.3.9 and 1.3.13')
if mibBuilder.loadTexts: cwaCallsBarred.setStatus('current')
if mibBuilder.loadTexts: cwaCallsBarred.setDescription('This variable indicates if this member can receive calls from or make calls to other members of the same CUG. When this variable is set to none(1), it means this CUG member can receive calls from and make calls to other members in the same CUG. When this variable is set to incoming(2), it means this member cannot receive incoming calls from other members in the same CUG. When this variable is set to outgoing(3), it means this member cannot make calls to other members in the same CUG. ')
cwaCugRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaCugRowStatus.setStatus('current')
if mibBuilder.loadTexts: cwaCugRowStatus.setDescription("The row status of each entry in this table. Once the 'cwaInterlockCode' is created, it cannot be modified. If the management station wants to assign a different Interlock Code to the same 'cwaCugIndex', the management station must remove the current entry and then add a new entry with the same 'cwaCugIndex' and a different 'cwaInterlockCode.")
cwaAddressCugTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1), )
if mibBuilder.loadTexts: cwaAddressCugTable.setReference('ITU-T Specification Q.2955.1 Section 1.3')
if mibBuilder.loadTexts: cwaAddressCugTable.setStatus('current')
if mibBuilder.loadTexts: cwaAddressCugTable.setDescription('A table of CUG parameters associated with each provisioned ATM address.')
cwaAddressCugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-WAN-ATM-CUG-MIB", "cwaAtmAddress"), (0, "CISCO-WAN-ATM-CUG-MIB", "cwaAddressLength"))
if mibBuilder.loadTexts: cwaAddressCugEntry.setStatus('current')
if mibBuilder.loadTexts: cwaAddressCugEntry.setDescription("The managed system will automatically create an entry in this table when the first CUG is created for the same ATM address in 'cwaCugTable'. A entry in this table is automatically destroyed by the managed system when all CUGs of the same ATM address are destroyed in the 'cwaCugTable'.")
cwaCugAtmAddressPlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1, 1), CiscoAtmAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwaCugAtmAddressPlan.setStatus('current')
if mibBuilder.loadTexts: cwaCugAtmAddressPlan.setDescription('This is the type of the ATM address associated with this entry.')
cwaIncomingAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notAllowed", 1), ("allowed", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwaIncomingAccess.setReference('ITU-T Specification Q.2955.1 section 1.3.8')
if mibBuilder.loadTexts: cwaIncomingAccess.setStatus('current')
if mibBuilder.loadTexts: cwaIncomingAccess.setDescription("This variable decides whether 'incoming access' is allowed for a CUG user. the 'incoming access' allows a CUG user to receive calls from all other non-CUG users and also from those other CUG user that allow 'outgoing access'. When the value is set to notAllowed(1), the 'incoming access' is not allowed. When the value is set to allowed(2), the 'incoming access' is allowed. When this entry is created, this variable has a value of notAllowed(1).")
cwaOutgoingAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notAllowed", 1), ("allowedPerCall", 2), ("allowedPermanently", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwaOutgoingAccess.setReference('ITU-T Specification Q.2955.1 section 1.3.9')
if mibBuilder.loadTexts: cwaOutgoingAccess.setStatus('current')
if mibBuilder.loadTexts: cwaOutgoingAccess.setDescription("This variable decides whether 'outgoing access' is allowed for a CUG user. The 'outgoing access' allows a member of a CUG to make calls to other non-CUG members and also to those other CUG members that allow 'incoming access'. When the value is set to notAllowed(1), the 'outgoinging access' is not allowed. When the value is set to allowedPerCall(2), the 'outgoing access' is granted on a per call basis. This means for each call, the 'outgoing access' request must be part of the call SETUP message. When the value is set to allowedPermanently(3), the 'outgoing access' is allowed for all calls. When this entry is created by the managed system, this variable has a value of notAllowed(1).")
cwaPreferentialCug = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwaPreferentialCug.setReference('ITU-T Specification Q.2955.1 section 1.3.14')
if mibBuilder.loadTexts: cwaPreferentialCug.setStatus('current')
if mibBuilder.loadTexts: cwaPreferentialCug.setDescription("The CUG index of the 'preferential CUG' for this address. There can be only one 'preferential CUG' for an address. A CUG user subscribing to 'preferential CUG' nominates a CUG index which the network uses as a default to identify the required CUG in the absence of any CUG information in the outgoing call request. A value of zero means the address does not have a preferential CUG. The value of this variable must correspond to a 'cwaCugIndex' of an entry in the 'cwaCugTable'. When an entry is created by the managed system, this variable has a value of 0. When selecting a 'preferential' CUG in the address's CUGs, the corresponding CUG must allow outgoing calls. This means 'cwaCallsBarred'(Outgoing Calls Barred) must not have a value of outgoing(2) for the corresponding CUG.")
ciscoWanAtmCugMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 3))
ciscoWanAtmCugMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 1))
ciscoWanAtmCugMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 2))
ciscoWanAtmCugMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 1, 1)).setObjects(("CISCO-WAN-ATM-CUG-MIB", "ciscoWanAtmCugGroup"), ("CISCO-WAN-ATM-CUG-MIB", "ciscoWanAtmAddressCugGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmCugMIBCompliance = ciscoWanAtmCugMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoWanAtmCugMIBCompliance.setDescription('The compliance statement for SNMPv2 entities which implement Closed User Groups(CUG).')
ciscoWanAtmCugGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 2, 1)).setObjects(("CISCO-WAN-ATM-CUG-MIB", "cwaAddressPlan"), ("CISCO-WAN-ATM-CUG-MIB", "cwaInterlockCode"), ("CISCO-WAN-ATM-CUG-MIB", "cwaCallsBarred"), ("CISCO-WAN-ATM-CUG-MIB", "cwaCugRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmCugGroup = ciscoWanAtmCugGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoWanAtmCugGroup.setDescription('This group contains the CUGs for each ATM address on the managed system.')
ciscoWanAtmAddressCugGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 2, 2)).setObjects(("CISCO-WAN-ATM-CUG-MIB", "cwaCugAtmAddressPlan"), ("CISCO-WAN-ATM-CUG-MIB", "cwaIncomingAccess"), ("CISCO-WAN-ATM-CUG-MIB", "cwaOutgoingAccess"), ("CISCO-WAN-ATM-CUG-MIB", "cwaPreferentialCug"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmAddressCugGroup = ciscoWanAtmAddressCugGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoWanAtmAddressCugGroup.setDescription('This group contains objects for the CUG for each ATM address on the managed system.')
mibBuilder.exportSymbols("CISCO-WAN-ATM-CUG-MIB", ciscoWanAtmCugMIBGroups=ciscoWanAtmCugMIBGroups, cwaCugEntry=cwaCugEntry, ciscoWanAtmAddressCugGroup=ciscoWanAtmAddressCugGroup, cwaCugRowStatus=cwaCugRowStatus, cwaInterlockCode=cwaInterlockCode, cwaCugMIBNotifications=cwaCugMIBNotifications, cwaCugIndex=cwaCugIndex, cwaIncomingAccess=cwaIncomingAccess, ciscoWanAtmCugMIBConformance=ciscoWanAtmCugMIBConformance, ciscoWanAtmCugMIBCompliance=ciscoWanAtmCugMIBCompliance, CiscoAtmAddressType=CiscoAtmAddressType, cwaCallsBarred=cwaCallsBarred, cwaCugAtmAddressPlan=cwaCugAtmAddressPlan, cwaAddressLength=cwaAddressLength, ciscoWanAtmCugMIBCompliances=ciscoWanAtmCugMIBCompliances, CiscoAtmInterlockCode=CiscoAtmInterlockCode, cwaCugTable=cwaCugTable, CiscoAtmAddressLength=CiscoAtmAddressLength, ciscoWanAtmCugGroup=ciscoWanAtmCugGroup, PYSNMP_MODULE_ID=ciscoWanAtmCugMIB, cwaPreferentialCug=cwaPreferentialCug, cwaAddressCugTable=cwaAddressCugTable, ciscoWanAtmCugMIB=ciscoWanAtmCugMIB, cwaOutgoingAccess=cwaOutgoingAccess, cwaCug=cwaCug, cwaAddressCug=cwaAddressCug, cwaAddressCugEntry=cwaAddressCugEntry, cwaCugMIBObjects=cwaCugMIBObjects, cwaAtmAddress=cwaAtmAddress, cwaAddressPlan=cwaAddressPlan)
