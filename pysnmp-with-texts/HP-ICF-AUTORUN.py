#
# PySNMP MIB module HP-ICF-AUTORUN (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-AUTORUN
# Produced by pysmi-0.3.4 at Wed May  1 13:33:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, IpAddress, MibIdentifier, Gauge32, Bits, Counter32, Unsigned32, TimeTicks, iso, Counter64, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "IpAddress", "MibIdentifier", "Gauge32", "Bits", "Counter32", "Unsigned32", "TimeTicks", "iso", "Counter64", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
hpicfAutorun = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42))
if mibBuilder.loadTexts: hpicfAutorun.setLastUpdated('200708240000Z')
if mibBuilder.loadTexts: hpicfAutorun.setOrganization('Hewlett-Packard Company, Workgroup Networks Division')
if mibBuilder.loadTexts: hpicfAutorun.setContactInfo('Hewlett Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfAutorun.setDescription('This MIB module manages Autorun configuration for devices in the HP Integrated Communication Facility product line.')
hpicfAutorunConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 1))
hpicfUsbAutorunEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUsbAutorunEnable.setStatus('current')
if mibBuilder.loadTexts: hpicfUsbAutorunEnable.setDescription('This MIB object identifies the admin status of the USB Autorun feature true(1) - Autorun Enabled. false(2) - Autorun Disabled.')
hpicfUsbAutorunSecureMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUsbAutorunSecureMode.setStatus('current')
if mibBuilder.loadTexts: hpicfUsbAutorunSecureMode.setDescription('This MIB object identifies the admin status of the secure-mode for the USB Autorun feature true(1) - secure-mode for autorun Enabled. false(2) - secure-mode for autorun Disabled.')
hpicfUsbAutorunEncryptionKey = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUsbAutorunEncryptionKey.setStatus('current')
if mibBuilder.loadTexts: hpicfUsbAutorunEncryptionKey.setDescription('This MIB object identifies the configured encryption key string for USB Autorun feature')
hpicfAutorunConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 2))
hpicfAutorunCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 2, 1))
hpicfAutorunGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 2, 2))
hpicfAutorunCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 2, 1, 1)).setObjects(("HP-ICF-AUTORUN", "hpicfAutorunConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfAutorunCompliance = hpicfAutorunCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfAutorunCompliance.setDescription('Compliance statement for HP ICP Autorun configuration')
hpicfAutorunConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 2, 2, 1)).setObjects(("HP-ICF-AUTORUN", "hpicfUsbAutorunEnable"), ("HP-ICF-AUTORUN", "hpicfUsbAutorunSecureMode"), ("HP-ICF-AUTORUN", "hpicfUsbAutorunEncryptionKey"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfAutorunConfigGroup = hpicfAutorunConfigGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfAutorunConfigGroup.setDescription(' ')
mibBuilder.exportSymbols("HP-ICF-AUTORUN", hpicfUsbAutorunEnable=hpicfUsbAutorunEnable, hpicfUsbAutorunEncryptionKey=hpicfUsbAutorunEncryptionKey, PYSNMP_MODULE_ID=hpicfAutorun, hpicfAutorunCompliance=hpicfAutorunCompliance, hpicfAutorun=hpicfAutorun, hpicfAutorunConformance=hpicfAutorunConformance, hpicfAutorunConfig=hpicfAutorunConfig, hpicfAutorunCompliances=hpicfAutorunCompliances, hpicfAutorunGroups=hpicfAutorunGroups, hpicfAutorunConfigGroup=hpicfAutorunConfigGroup, hpicfUsbAutorunSecureMode=hpicfUsbAutorunSecureMode)
