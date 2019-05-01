#
# PySNMP MIB module CISCO-CIRCUIT-INTERFACE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CIRCUIT-INTERFACE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:53:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, Bits, Counter64, Integer32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, IpAddress, NotificationType, Gauge32, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Counter64", "Integer32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "IpAddress", "NotificationType", "Gauge32", "MibIdentifier", "Counter32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ciscoCircuitInterfaceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 160))
ciscoCircuitInterfaceMIB.setRevisions(('2000-05-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCircuitInterfaceMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCircuitInterfaceMIB.setLastUpdated('200005090000Z')
if mibBuilder.loadTexts: ciscoCircuitInterfaceMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCircuitInterfaceMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoCircuitInterfaceMIB.setDescription('The MIB module to configure the circuit description for an interface. The circuit description can be used to describe and identify circuits on interfaces like ATM, frame-relay etc.')
ciscoCircuitInterfaceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 160, 1))
cciDescription = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1))
cciDescriptionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1, 1), )
if mibBuilder.loadTexts: cciDescriptionTable.setStatus('current')
if mibBuilder.loadTexts: cciDescriptionTable.setDescription('This table contains a circuit description to identify circuit based interfaces like ATM, Frame-Relay etc. The circuit description could be used for example, to correlate performance statistics associated with the corresponding interfaces.')
cciDescriptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cciDescriptionEntry.setStatus('current')
if mibBuilder.loadTexts: cciDescriptionEntry.setDescription('Each cciDescriptionEntry contains the circuit description for a particular circuit based interface. The entry is identified by the ifIndex which would typically correspond to circuit based interfaces. Interfaces with ifType equal to atm(37), frameRelay(32) frameRelayService(44) are some examples. Entries can only be created by management station action. Entries can be deleted by setting the cciStatus object to destroy(6). The agent will delete any cciEntry if the corresponding ifEntry is deleted. Entries are not maintained in any kind of NV-storage, and will not be recreated by the agent after a reboot.')
cciDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cciDescr.setStatus('current')
if mibBuilder.loadTexts: cciDescr.setDescription('The circuit description of the interface. It has no default value.')
cciStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cciStatus.setStatus('current')
if mibBuilder.loadTexts: cciStatus.setDescription('The row status object, but with restricted values. Only two values are allowed for this object: createAndGo(4) and destroy(6). The row is created by specifying the value for cciDescr and setting this object to createAndGo(4). If the row creation is succesfull, the cciStatus would be active(1). In the active(1) state, the cciDescr can be modifed. The row is deleted by setting this object to destroy(6).')
ciscoCircuitInterfaceMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 160, 3))
ciscoCircuitInterfaceMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 160, 3, 1))
ciscoCircuitInterfaceMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 160, 3, 2))
ciscoCircuitInterfaceMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 160, 3, 1, 1)).setObjects(("CISCO-CIRCUIT-INTERFACE-MIB", "ciscoCircuitInterfaceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCircuitInterfaceMIBCompliance = ciscoCircuitInterfaceMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoCircuitInterfaceMIBCompliance.setDescription('The compliance statement for Cisco agents which implement the Cisco Circuit Interface MIB.')
ciscoCircuitInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 160, 3, 2, 1)).setObjects(("CISCO-CIRCUIT-INTERFACE-MIB", "cciDescr"), ("CISCO-CIRCUIT-INTERFACE-MIB", "cciStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCircuitInterfaceGroup = ciscoCircuitInterfaceGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCircuitInterfaceGroup.setDescription('The Cisco Circuit Interface MIB objects.')
mibBuilder.exportSymbols("CISCO-CIRCUIT-INTERFACE-MIB", ciscoCircuitInterfaceMIBCompliances=ciscoCircuitInterfaceMIBCompliances, ciscoCircuitInterfaceMIBObjects=ciscoCircuitInterfaceMIBObjects, cciDescriptionTable=cciDescriptionTable, cciStatus=cciStatus, ciscoCircuitInterfaceMIBConformance=ciscoCircuitInterfaceMIBConformance, PYSNMP_MODULE_ID=ciscoCircuitInterfaceMIB, ciscoCircuitInterfaceGroup=ciscoCircuitInterfaceGroup, cciDescription=cciDescription, ciscoCircuitInterfaceMIBGroups=ciscoCircuitInterfaceMIBGroups, cciDescriptionEntry=cciDescriptionEntry, ciscoCircuitInterfaceMIBCompliance=ciscoCircuitInterfaceMIBCompliance, ciscoCircuitInterfaceMIB=ciscoCircuitInterfaceMIB, cciDescr=cciDescr)
