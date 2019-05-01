#
# PySNMP MIB module CISCO-L2L3-INTERFACE-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-L2L3-INTERFACE-CONFIG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:04:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, Counter32, IpAddress, NotificationType, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, MibIdentifier, Integer32, Counter64, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "IpAddress", "NotificationType", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "MibIdentifier", "Integer32", "Counter64", "ModuleIdentity", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoL2L3IfConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 151))
ciscoL2L3IfConfigMIB.setRevisions(('2000-05-10 19:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoL2L3IfConfigMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoL2L3IfConfigMIB.setLastUpdated('200005101900Z')
if mibBuilder.loadTexts: ciscoL2L3IfConfigMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoL2L3IfConfigMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoL2L3IfConfigMIB.setDescription('Interface switchport mode configuration management MIB. This MIB is used to monitor and control configuration of interface switchport and routed mode.')
ciscoL2L3IfConfigMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 151, 1))
cL2L3IfConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1))
class CL2L3InterfaceMode(TextualConvention, Integer32):
    description = "The operational mode of the interface. For administrative and operational states, valid values are: routed(1), switchport(2). routed(1): Routed mode interfaces direct traffic using layer 3 protocols. switchport(2): Switchport-mode interfaces direct traffic using layer 2 protocols. A switchport-mode interface can be in access mode, or trunk mode, or multi-mode. Switchport interface operating mode can be configured manually, or negotiated by Dynamic Trunking Protocol (DTP) or Dynamic Inter-Switch Link (DISL). Access-mode interfaces carry one VLAN's traffic. Access-mode interface parameters are configured in CISCO-VLAN-MEMBERSHIP-MIB. Trunk-mode interfaces carry one or more VLANs. VLAN-related trunk-mode interface parameters are configured in CISCO-VTP-MIB. Multi-mode interfaces carry one VLAN to each alias of a single connected end-station. VLAN-related multi-mode interface parameters are configured in CISCO-VTP-MIB. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("routed", 1), ("switchport", 2))

cL2L3IfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1), )
if mibBuilder.loadTexts: cL2L3IfTable.setStatus('current')
if mibBuilder.loadTexts: cL2L3IfTable.setDescription('The table shows the administratively requested and actual operating configuration for switchport interfaces.')
cL2L3IfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cL2L3IfEntry.setStatus('current')
if mibBuilder.loadTexts: cL2L3IfEntry.setDescription('An entry represents the configuration and operation of a switchport interface. Entries are created and deleted automatically in tandem with the corresponding ifEntries.')
cL2L3IfModeAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1, 1, 1), CL2L3InterfaceMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cL2L3IfModeAdmin.setStatus('current')
if mibBuilder.loadTexts: cL2L3IfModeAdmin.setDescription('The administratively desired interface mode.')
cL2L3IfModeOper = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1, 1, 2), CL2L3InterfaceMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cL2L3IfModeOper.setStatus('current')
if mibBuilder.loadTexts: cL2L3IfModeOper.setDescription('The operational interface mode.')
ciscoL2L3IfConfigMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 151, 3))
ciscoL2L3IfConfigMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 1))
ciscoL2L3IfConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 2))
ciscoL2L3IfConfigMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 1, 1)).setObjects(("CISCO-L2L3-INTERFACE-CONFIG-MIB", "ciscoL2L3IfConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigMIBCompliance = ciscoL2L3IfConfigMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoL2L3IfConfigMIBCompliance.setDescription('The compliance statement for entities which implement the Cisco L2L3 Interface Configuration Management MIB')
ciscoL2L3IfConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 2, 1)).setObjects(("CISCO-L2L3-INTERFACE-CONFIG-MIB", "cL2L3IfModeAdmin"), ("CISCO-L2L3-INTERFACE-CONFIG-MIB", "cL2L3IfModeOper"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigMIBGroup = ciscoL2L3IfConfigMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoL2L3IfConfigMIBGroup.setDescription('Interface L2 & L3 mode objects')
mibBuilder.exportSymbols("CISCO-L2L3-INTERFACE-CONFIG-MIB", ciscoL2L3IfConfigMIBGroup=ciscoL2L3IfConfigMIBGroup, CL2L3InterfaceMode=CL2L3InterfaceMode, cL2L3IfEntry=cL2L3IfEntry, cL2L3IfModeOper=cL2L3IfModeOper, ciscoL2L3IfConfigMIBCompliance=ciscoL2L3IfConfigMIBCompliance, ciscoL2L3IfConfigMIBGroups=ciscoL2L3IfConfigMIBGroups, cL2L3IfTable=cL2L3IfTable, ciscoL2L3IfConfigMIBObjects=ciscoL2L3IfConfigMIBObjects, ciscoL2L3IfConfigMIBCompliances=ciscoL2L3IfConfigMIBCompliances, PYSNMP_MODULE_ID=ciscoL2L3IfConfigMIB, ciscoL2L3IfConfigMIBConformance=ciscoL2L3IfConfigMIBConformance, cL2L3IfModeAdmin=cL2L3IfModeAdmin, ciscoL2L3IfConfigMIB=ciscoL2L3IfConfigMIB, cL2L3IfConfig=cL2L3IfConfig)
