#
# PySNMP MIB module HP-ICF-AUTORUN (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-AUTORUN
# Produced by pysmi-0.3.4 at Mon Apr 29 19:20:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Bits, Counter32, ModuleIdentity, Counter64, Unsigned32, Gauge32, Integer32, NotificationType, iso, TimeTicks, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "Counter32", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "Integer32", "NotificationType", "iso", "TimeTicks", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
hpicfAutorun = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42))
if mibBuilder.loadTexts: hpicfAutorun.setLastUpdated('200708240000Z')
if mibBuilder.loadTexts: hpicfAutorun.setOrganization('Hewlett-Packard Company, Workgroup Networks Division')
hpicfAutorunConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 1))
hpicfUsbAutorunEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUsbAutorunEnable.setStatus('current')
hpicfUsbAutorunSecureMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUsbAutorunSecureMode.setStatus('current')
hpicfUsbAutorunEncryptionKey = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUsbAutorunEncryptionKey.setStatus('current')
hpicfAutorunConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 2))
hpicfAutorunCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 2, 1))
hpicfAutorunGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 2, 2))
hpicfAutorunCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 2, 1, 1)).setObjects(("HP-ICF-AUTORUN", "hpicfAutorunConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfAutorunCompliance = hpicfAutorunCompliance.setStatus('current')
hpicfAutorunConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 2, 2, 1)).setObjects(("HP-ICF-AUTORUN", "hpicfUsbAutorunEnable"), ("HP-ICF-AUTORUN", "hpicfUsbAutorunSecureMode"), ("HP-ICF-AUTORUN", "hpicfUsbAutorunEncryptionKey"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfAutorunConfigGroup = hpicfAutorunConfigGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-AUTORUN", PYSNMP_MODULE_ID=hpicfAutorun, hpicfUsbAutorunEnable=hpicfUsbAutorunEnable, hpicfAutorunConfigGroup=hpicfAutorunConfigGroup, hpicfUsbAutorunSecureMode=hpicfUsbAutorunSecureMode, hpicfUsbAutorunEncryptionKey=hpicfUsbAutorunEncryptionKey, hpicfAutorunCompliance=hpicfAutorunCompliance, hpicfAutorun=hpicfAutorun, hpicfAutorunConformance=hpicfAutorunConformance, hpicfAutorunConfig=hpicfAutorunConfig, hpicfAutorunCompliances=hpicfAutorunCompliances, hpicfAutorunGroups=hpicfAutorunGroups)
