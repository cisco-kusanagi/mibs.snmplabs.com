#
# PySNMP MIB module CISCO-POE-PD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-POE-PD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:52:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Integer32, iso, ModuleIdentity, Counter32, NotificationType, ObjectIdentity, Gauge32, Bits, MibIdentifier, IpAddress, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "iso", "ModuleIdentity", "Counter32", "NotificationType", "ObjectIdentity", "Gauge32", "Bits", "MibIdentifier", "IpAddress", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoPoePdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 414))
ciscoPoePdMIB.setRevisions(('2004-05-05 00:00',))
if mibBuilder.loadTexts: ciscoPoePdMIB.setLastUpdated('200405050000Z')
if mibBuilder.loadTexts: ciscoPoePdMIB.setOrganization('Cisco Systems Inc.')
cpoePdMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 0))
cpoePdMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 1))
cpoePdMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 2))
cpoePdInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1))
class CpoePdPowerSourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("pending", 1), ("acAdaptor", 2), ("thirdParty", 3), ("classic", 4), ("midspan", 5), ("cdpNegotiated", 6), ("highPowerClassic", 7))

cpoePdCurrentPowerLevel = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpoePdCurrentPowerLevel.setStatus('current')
cpoePdCurrentPowerSource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 2), CpoePdPowerSourceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpoePdCurrentPowerSource.setStatus('current')
cpoePdSupportedPowerLevelTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3), )
if mibBuilder.loadTexts: cpoePdSupportedPowerLevelTable.setStatus('current')
cpoePdSupportedPowerLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-POE-PD-MIB", "cpoePdSupportedPowerLevel"))
if mibBuilder.loadTexts: cpoePdSupportedPowerLevelEntry.setStatus('current')
cpoePdSupportedPowerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: cpoePdSupportedPowerLevel.setStatus('current')
cpoePdSupportedPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setUnits('milliwatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: cpoePdSupportedPower.setStatus('current')
cpoePdSupportedPowerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpoePdSupportedPowerMode.setStatus('current')
cpoePdMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 1))
cpoePdMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 2))
cpoePdMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 1, 1)).setObjects(("CISCO-POE-PD-MIB", "cpoePdInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpoePdMIBCompliance = cpoePdMIBCompliance.setStatus('current')
cpoePdInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 2, 1)).setObjects(("CISCO-POE-PD-MIB", "cpoePdCurrentPowerLevel"), ("CISCO-POE-PD-MIB", "cpoePdCurrentPowerSource"), ("CISCO-POE-PD-MIB", "cpoePdSupportedPower"), ("CISCO-POE-PD-MIB", "cpoePdSupportedPowerMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpoePdInformationGroup = cpoePdInformationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-POE-PD-MIB", cpoePdMIBConformance=cpoePdMIBConformance, cpoePdMIBCompliance=cpoePdMIBCompliance, PYSNMP_MODULE_ID=ciscoPoePdMIB, cpoePdSupportedPower=cpoePdSupportedPower, cpoePdCurrentPowerLevel=cpoePdCurrentPowerLevel, cpoePdSupportedPowerLevel=cpoePdSupportedPowerLevel, cpoePdMIBObjects=cpoePdMIBObjects, CpoePdPowerSourceType=CpoePdPowerSourceType, cpoePdSupportedPowerLevelEntry=cpoePdSupportedPowerLevelEntry, ciscoPoePdMIB=ciscoPoePdMIB, cpoePdSupportedPowerLevelTable=cpoePdSupportedPowerLevelTable, cpoePdMIBCompliances=cpoePdMIBCompliances, cpoePdMIBGroups=cpoePdMIBGroups, cpoePdInformation=cpoePdInformation, cpoePdInformationGroup=cpoePdInformationGroup, cpoePdCurrentPowerSource=cpoePdCurrentPowerSource, cpoePdSupportedPowerMode=cpoePdSupportedPowerMode, cpoePdMIBNotifications=cpoePdMIBNotifications)
