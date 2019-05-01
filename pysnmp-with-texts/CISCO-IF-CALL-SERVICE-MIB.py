#
# PySNMP MIB module CISCO-IF-CALL-SERVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IF-CALL-SERVICE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:01:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
BulkConfigResult, ConfigIterator = mibBuilder.importSymbols("CISCO-TC", "BulkConfigResult", "ConfigIterator")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
OwnerString, = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Gauge32, IpAddress, Unsigned32, TimeTicks, Counter32, ModuleIdentity, NotificationType, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "Unsigned32", "TimeTicks", "Counter32", "ModuleIdentity", "NotificationType", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIfCallServiceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 9968))
ciscoIfCallServiceMIB.setRevisions(('2003-04-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIfCallServiceMIB.setRevisionsDescriptions(('Initial version of the MIB module.',))
if mibBuilder.loadTexts: ciscoIfCallServiceMIB.setLastUpdated('200304250000Z')
if mibBuilder.loadTexts: ciscoIfCallServiceMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIfCallServiceMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoIfCallServiceMIB.setDescription('The MIB is used to manage call service state for interfaces on media gateway. ')
ciscoIfCallServiceMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 0))
ciscoIfCallServiceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1))
ciscoIfCallServiceMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 2))
cicServiceConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1))
class CIfCallServiceOperState(TextualConvention, Integer32):
    description = 'This Textual Convention defines the call connection related service state of an interface. The possible service states are: inService: An interface is ready for call connection setup. outOfService: The interface is in Out-Of-Service state. All calls will be destroyed on this interface by Call Agent. A call service state change message with FORCED method is sent to Call Agent. No new connections are allowed on the interface. oosPending: The interface is in Out-Of-Service state. All existing calls will not be affected on this interface. A call service state change message with GRACEFUL method is sent to Call Agent. No new connections are allowed. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inService", 1), ("outOfService", 2), ("oosPending", 3))

class CIfCallServiceAdminState(TextualConvention, Integer32):
    description = 'This Textual Convention defines the service administrative state of an interface. The possible service administrative states are as follows: inService: The interface would be restored to in-service status and a call service state change with method RESTART message will be sent to Call Agent forcefulOutOfService: The interface would be in Out-Of-Service state. Any existing connections on the interface will deleted. A call service state change message with FORCED method will be sent to Call Agent. New connections would be blocked. gracefulOutOfService: The interface would be in Out-Of-Service state. Any existing connections on the interface are not affected. A call service state change message with GRACEFUL method will be sent to Call Agent. New connections would be blocked. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inService", 1), ("forcedOutOfService", 2), ("gracefulOutOfService", 3))

cicServiceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1), )
if mibBuilder.loadTexts: cicServiceTable.setStatus('current')
if mibBuilder.loadTexts: cicServiceTable.setDescription('This table defines the parameters related to the call service state administration for the interfaces on media gateway. The possible interfaces include channelized sonet interface, DS1 interface, etc.. ')
cicServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cicServiceEntry.setStatus('current')
if mibBuilder.loadTexts: cicServiceEntry.setDescription('An entry containing service administration information applicable to a particular interface. ')
cicServiceOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 1), CIfCallServiceOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicServiceOperState.setStatus('current')
if mibBuilder.loadTexts: cicServiceOperState.setDescription("This object indicates the current operating state of the service in the interface. The entry in this table is also in ifTable(the index of this table is ifIndex). The 'cicServiceOperState' of the entry is not only dependent on the 'cicServiceAdminState', it is also dependent on the 'ifOperStatus' of ifTable. The following is the relationship between 'cicServiceAdminState' and 'ifOperStatus': cicServiceOperState cicServiceAdminState ifOperStatus ---------------- ----------------- ------------ inService inService up outOfService forcefulOutOfService up oosPending gracefulOutOfService up outOfService inService down outOfService forcefulOutOfService down outOfService gracefulOutOfService down ")
cicServiceAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 2), CIfCallServiceAdminState().clone('inService')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicServiceAdminState.setStatus('current')
if mibBuilder.loadTexts: cicServiceAdminState.setDescription("This object is used to change the desired service state of the interface. The operational service state of the interface is indicated by 'cicServiceOperState'. ")
cicServiceGraceTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicServiceGraceTime.setStatus('current')
if mibBuilder.loadTexts: cicServiceGraceTime.setDescription("This object specifies the amount of time before the existing call connections been gracefully shutdown in the interface when 'cicServiceAdminState' is set to 'gracefulOutOfService'. This object is not applicable if 'cicServiceAdminState' is set to 'forcefulOutOfService'. The value of 0 specifies that the service on the interface will not be put outOfService until the call connection over the interface is terminated. ")
cicServiceRepetition = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 4), ConfigIterator().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicServiceRepetition.setStatus('current')
if mibBuilder.loadTexts: cicServiceRepetition.setDescription('This object is used to change service state to multiple interfaces by repeatedly applying the writable objects of cicServiceTable specified in the same SNMP PDU starting from the row specified by the instance value in INDEX for the number of rows specified in this object. The order of operation is iterated through the logical order of the interface. Whether the iteration will be applied across the physical boundary or not is depends upon the system implementation. The GET operation on this object will always return 1.')
cicServiceRepeatOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 5), OwnerString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicServiceRepeatOwner.setStatus('current')
if mibBuilder.loadTexts: cicServiceRepeatOwner.setDescription("This object is used for error checking of the operation specified in 'cicServiceRepetition'. The value of this object is set by the SNMP manager with its own identifier at the same time as issuing the bulk operation by setting 'cicServiceRepetition'. This object and 'cicServiceRepetition' need to be in the same SNMP SET PDU. Later on, the SNMP manager should check the value of this object, if it is same as the name previously set, then the value of 'cicServiceRepeatResult' indicates the result of the bulk operation initiated by this SNMP manager. In the case that a SNMP manager do multi bulk operation, it is recommended that the SNMP manager choose to set this value to its IP Address so as to be unique. ")
cicServiceRepeatResult = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 6), BulkConfigResult()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicServiceRepeatResult.setStatus('current')
if mibBuilder.loadTexts: cicServiceRepeatResult.setDescription("This object is used for error checking of the operation specified in cicServiceRepetition. This object indicates the result of the bulk operation initiated by the SNMP manager specified in the value of 'cicServiceRepeatOwner'. ")
cicServiceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 2, 1))
cicServiceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 2, 2))
cicServiceCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 9968, 2, 1, 1)).setObjects(("CISCO-IF-CALL-SERVICE-MIB", "cicServiceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cicServiceCompliance = cicServiceCompliance.setStatus('current')
if mibBuilder.loadTexts: cicServiceCompliance.setDescription('The compliance statement for interfaces which implement the CISCO-IF-CALL-SERVICE-MIB.')
cicServiceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9968, 2, 2, 1)).setObjects(("CISCO-IF-CALL-SERVICE-MIB", "cicServiceOperState"), ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceAdminState"), ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceGraceTime"), ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceRepetition"), ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceRepeatOwner"), ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceRepeatResult"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cicServiceGroup = cicServiceGroup.setStatus('current')
if mibBuilder.loadTexts: cicServiceGroup.setDescription('A collection of objects for managing per interface basis call service state information. ')
mibBuilder.exportSymbols("CISCO-IF-CALL-SERVICE-MIB", ciscoIfCallServiceMIB=ciscoIfCallServiceMIB, cicServiceGroup=cicServiceGroup, PYSNMP_MODULE_ID=ciscoIfCallServiceMIB, cicServiceCompliance=cicServiceCompliance, ciscoIfCallServiceMIBConformance=ciscoIfCallServiceMIBConformance, ciscoIfCallServiceMIBObjects=ciscoIfCallServiceMIBObjects, cicServiceGraceTime=cicServiceGraceTime, cicServiceEntry=cicServiceEntry, cicServiceRepeatResult=cicServiceRepeatResult, cicServiceGroups=cicServiceGroups, CIfCallServiceAdminState=CIfCallServiceAdminState, cicServiceCompliances=cicServiceCompliances, cicServiceOperState=cicServiceOperState, cicServiceRepeatOwner=cicServiceRepeatOwner, cicServiceConfig=cicServiceConfig, cicServiceAdminState=cicServiceAdminState, cicServiceRepetition=cicServiceRepetition, CIfCallServiceOperState=CIfCallServiceOperState, ciscoIfCallServiceMIBNotifs=ciscoIfCallServiceMIBNotifs, cicServiceTable=cicServiceTable)
