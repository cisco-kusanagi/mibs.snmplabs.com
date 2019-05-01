#
# PySNMP MIB module CISCO-SWITCH-FABRIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SWITCH-FABRIC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:13:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
PhysicalIndex, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter32, Gauge32, iso, ObjectIdentity, MibIdentifier, Bits, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "Gauge32", "iso", "ObjectIdentity", "MibIdentifier", "Bits", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Unsigned32", "NotificationType")
DisplayString, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TruthValue", "TextualConvention")
ciscoSwitchFabricMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 803))
ciscoSwitchFabricMIB.setRevisions(('2014-07-30 00:00', '2012-06-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSwitchFabricMIB.setRevisionsDescriptions(('Added the following OBJECT-GROUP - csfFabricCrcErrorNotifsControlGroup - csfFabricCrcErrorNotifsInfoGroup - csfFabricCrcErrorNotifsGroup. Added new compliance csfSwitchFabricMIBCompliance1.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSwitchFabricMIB.setLastUpdated('201407300000Z')
if mibBuilder.loadTexts: ciscoSwitchFabricMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSwitchFabricMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSwitchFabricMIB.setDescription('This MIB module defined managed objects that facilitates the management of switching fabric information in a Cisco switch.')
ciscoSwitchFabricMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 0))
ciscoSwitchFabricMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 1))
ciscoSwitchFabricMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 2))
csfFabricStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1))
csfNotifsControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 2))
csfNotifsOnlyInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 3))
class CsfFabricLinkType(TextualConvention, Integer32):
    description = 'The type of fabric link. other - none of the following qEngineFacingLcXbarLink - queue engine facing linecard crossbar link fabricXbarLink - fabric module crossbar link fabricFacingLcXbarLink - fabric module facing linecard crossbar link lcXbarInterLink - linecard crossbar interlink fabricXbarInterLink - fabric module crossbar interlink centralXbarLink - central fabric link'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("qEngineFacingLcXbarLink", 2), ("fabricXbarLink", 3), ("fabricFacingLcXbarLink", 4), ("lcXbarInterLink", 5), ("fabricXbarInterLink", 6), ("centralXbarLink", 7))

class CsfPercentOrMinusOne(TextualConvention, Integer32):
    description = 'An integer that is in the range of a percent value. A value of -1 means that the percentage is not available.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100), )
csfFabricUtilTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1), )
if mibBuilder.loadTexts: csfFabricUtilTable.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilTable.setDescription('A table containing fabric utilization information.')
csfFabricUtilEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilLinkType"), (0, "CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilIndex"))
if mibBuilder.loadTexts: csfFabricUtilEntry.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilEntry.setDescription('A conceptual row containing the fabric utilization information for a particular type of traffic utilization of a fabric entity. An entry of this table is created if a traffic utilization on a fabric entity is detected by the managed system. An entry of this table is deleted when the removal of fabric entity.')
csfFabricUtilLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 1), CsfFabricLinkType())
if mibBuilder.loadTexts: csfFabricUtilLinkType.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilLinkType.setDescription('This object indicates the type of fabric link on which fabric traffic utilization is monitored.')
csfFabricUtilIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: csfFabricUtilIndex.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilIndex.setDescription('This object indicates an arbitrary integer value which uniquely identifies the type of traffic utilization.')
csfFabricUtilDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilDescr.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilDescr.setDescription('This object indicates the human-readable description of the type of fabric traffic utilization.')
csfFabricUtilBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 4), Unsigned32()).setUnits('gigabits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilBandwidth.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilBandwidth.setDescription('This object indicates the bandwidth of the fabric link.')
csfFabricUtilIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 5), CsfPercentOrMinusOne()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilIn.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilIn.setDescription('This object indicates the utilization on the fabric link input.')
csfFabricUtilInPeak = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 6), CsfPercentOrMinusOne()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilInPeak.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilInPeak.setDescription('This object indicates the peak utilization on the fabric link input.')
csfFabricUtilInPeakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilInPeakTime.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilInPeakTime.setDescription("This object indicates the time of the most recent change in the corresponding instance value of csfFabricUtilInPeak. This object contains value 0x0000010100000000 when the corresponding instance value of csfFabricUtilInPeak is '0 or '-1'.")
csfFabricUtilOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 8), CsfPercentOrMinusOne()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilOut.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilOut.setDescription('This object indicates the utilization on the fabric link output.')
csfFabricUtilOutPeak = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 9), CsfPercentOrMinusOne()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilOutPeak.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilOutPeak.setDescription('This object indicates the peak utilization on the fabric link output.')
csfFabricUtilOutPeakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilOutPeakTime.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilOutPeakTime.setDescription("This object indicates the time of the most recent change in the corresponding instance value of csfFabricUtilOutPeak. This object contains value 0x0000010100000000 when the corresponding instance value of csfFabricUtilInPeak is '0 or '-1'.")
csfFabricCrcErrorNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 2, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csfFabricCrcErrorNotifEnable.setStatus('current')
if mibBuilder.loadTexts: csfFabricCrcErrorNotifEnable.setDescription("This object specifies whether the system generates the cfsFabricCrcErrorNotif. A value of 'false' will prevent cfsFabricCrcErrorNotif notifications from being generated by this system.")
csfFabricCrcErrorEntPhysicalIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 3, 1), PhysicalIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: csfFabricCrcErrorEntPhysicalIndex.setStatus('current')
if mibBuilder.loadTexts: csfFabricCrcErrorEntPhysicalIndex.setDescription('This object indicates the entPhysicalIndex of the fabric entity on which fabric CRC error happens.')
csfFabricCrcErrorDescr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 3, 2), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: csfFabricCrcErrorDescr.setStatus('current')
if mibBuilder.loadTexts: csfFabricCrcErrorDescr.setDescription('This object indicates the fabric CRC error description. A zero-length string indicates that the error description is not available.')
csfFabricCrcErrorNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 803, 0, 1)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorEntPhysicalIndex"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorDescr"))
if mibBuilder.loadTexts: csfFabricCrcErrorNotif.setStatus('current')
if mibBuilder.loadTexts: csfFabricCrcErrorNotif.setDescription('A cfsFabricCrcErrorNotif is generated when fabric CRC errors are detected by the managed system.')
csfSwitchFabricMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 1))
csfSwitchFabricMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 2))
csfSwitchFabricMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 1, 1)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csfSwitchFabricMIBCompliance = csfSwitchFabricMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: csfSwitchFabricMIBCompliance.setDescription('The compliance statement for the CISCO-SWITCH-FABRIC-MIB.')
csfSwitchFabricMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 1, 2)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilGroup"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorNotifsControlGroup"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorNotifsInfoGroup"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csfSwitchFabricMIBCompliance1 = csfSwitchFabricMIBCompliance1.setStatus('current')
if mibBuilder.loadTexts: csfSwitchFabricMIBCompliance1.setDescription('The compliance statement for the CISCO-SWITCH-FABRIC-MIB.')
csfFabricUtilGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 2, 1)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilDescr"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilBandwidth"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilIn"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilInPeak"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilInPeakTime"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilOut"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilOutPeak"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilOutPeakTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csfFabricUtilGroup = csfFabricUtilGroup.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilGroup.setDescription('A collection of objects providing the information about utilization on the fabric link.')
csfFabricCrcErrorNotifsControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 2, 2)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csfFabricCrcErrorNotifsControlGroup = csfFabricCrcErrorNotifsControlGroup.setStatus('current')
if mibBuilder.loadTexts: csfFabricCrcErrorNotifsControlGroup.setDescription('A collection of objects providing notification control for csfFabricCrcErrorNotif.')
csfFabricCrcErrorNotifsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 2, 3)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorEntPhysicalIndex"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csfFabricCrcErrorNotifsInfoGroup = csfFabricCrcErrorNotifsInfoGroup.setStatus('current')
if mibBuilder.loadTexts: csfFabricCrcErrorNotifsInfoGroup.setDescription('A collection of object(s) providing the variable binding for csfFabricCrcErrorNotif.')
csfFabricCrcErrorNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 2, 4)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csfFabricCrcErrorNotifsGroup = csfFabricCrcErrorNotifsGroup.setStatus('current')
if mibBuilder.loadTexts: csfFabricCrcErrorNotifsGroup.setDescription('A collection of Fabric CRC Error notifications for CISCO-SWITCH-FABRIC-MIB.')
mibBuilder.exportSymbols("CISCO-SWITCH-FABRIC-MIB", csfFabricCrcErrorNotifsControlGroup=csfFabricCrcErrorNotifsControlGroup, csfSwitchFabricMIBCompliance=csfSwitchFabricMIBCompliance, csfFabricUtilOutPeakTime=csfFabricUtilOutPeakTime, csfFabricStatistics=csfFabricStatistics, PYSNMP_MODULE_ID=ciscoSwitchFabricMIB, csfFabricUtilDescr=csfFabricUtilDescr, csfSwitchFabricMIBGroups=csfSwitchFabricMIBGroups, csfFabricCrcErrorDescr=csfFabricCrcErrorDescr, csfFabricUtilTable=csfFabricUtilTable, csfFabricUtilEntry=csfFabricUtilEntry, csfNotifsControl=csfNotifsControl, ciscoSwitchFabricMIB=ciscoSwitchFabricMIB, csfFabricCrcErrorNotifEnable=csfFabricCrcErrorNotifEnable, csfSwitchFabricMIBCompliance1=csfSwitchFabricMIBCompliance1, ciscoSwitchFabricMIBObjects=ciscoSwitchFabricMIBObjects, csfFabricUtilOutPeak=csfFabricUtilOutPeak, csfFabricUtilIndex=csfFabricUtilIndex, csfSwitchFabricMIBCompliances=csfSwitchFabricMIBCompliances, csfFabricCrcErrorNotifsInfoGroup=csfFabricCrcErrorNotifsInfoGroup, csfNotifsOnlyInfo=csfNotifsOnlyInfo, csfFabricUtilLinkType=csfFabricUtilLinkType, csfFabricUtilOut=csfFabricUtilOut, csfFabricCrcErrorNotifsGroup=csfFabricCrcErrorNotifsGroup, csfFabricCrcErrorNotif=csfFabricCrcErrorNotif, csfFabricCrcErrorEntPhysicalIndex=csfFabricCrcErrorEntPhysicalIndex, CsfFabricLinkType=CsfFabricLinkType, csfFabricUtilInPeakTime=csfFabricUtilInPeakTime, csfFabricUtilIn=csfFabricUtilIn, ciscoSwitchFabricMIBConform=ciscoSwitchFabricMIBConform, csfFabricUtilInPeak=csfFabricUtilInPeak, csfFabricUtilBandwidth=csfFabricUtilBandwidth, ciscoSwitchFabricMIBNotifs=ciscoSwitchFabricMIBNotifs, CsfPercentOrMinusOne=CsfPercentOrMinusOne, csfFabricUtilGroup=csfFabricUtilGroup)
