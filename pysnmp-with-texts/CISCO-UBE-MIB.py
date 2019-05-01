#
# PySNMP MIB module CISCO-UBE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UBE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:14:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, MibIdentifier, IpAddress, ObjectIdentity, TimeTicks, Counter64, ModuleIdentity, Unsigned32, Counter32, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "MibIdentifier", "IpAddress", "ObjectIdentity", "TimeTicks", "Counter64", "ModuleIdentity", "Unsigned32", "Counter32", "iso", "NotificationType")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoUbeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 764))
ciscoUbeMIB.setRevisions(('2010-11-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoUbeMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoUbeMIB.setLastUpdated('201011290000Z')
if mibBuilder.loadTexts: ciscoUbeMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoUbeMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-cube@cisco.com')
if mibBuilder.loadTexts: ciscoUbeMIB.setDescription('This MIB describes objects used for managing Cisco Unified Border Element (CUBE). The Cisco Unified Border Element (CUBE) is a Cisco IOS Session Border Controller (SBC) that interconnects independent voice over IP (VoIP) and video over IP networks for data, voice, and video transport')
ciscoUbeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 764, 0))
ciscoUbeMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 764, 1))
cubeEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 764, 0, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cubeEnabled.setStatus('current')
if mibBuilder.loadTexts: cubeEnabled.setDescription("This object represents, whether the Cisco Unified Border Element (CUBE) is enabled on the device or not. The value 'true' means that the CUBE feature is enabled on the device. The value 'false' means that the CUBE feature is disabled.")
cubeVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 764, 0, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cubeVersion.setStatus('current')
if mibBuilder.loadTexts: cubeVersion.setDescription('This object represents the version of Cisco Unified Border Element on the device.')
cubeTotalSessionAllowed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 764, 0, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 999999))).setUnits('session').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cubeTotalSessionAllowed.setStatus('current')
if mibBuilder.loadTexts: cubeTotalSessionAllowed.setDescription('This object provides the total number of CUBE session allowed on the device. The value zero means no sessions are allowed with CUBE.')
ciscoUbeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 1))
ciscoUbeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 2))
ciscoCubeMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 1, 1)).setObjects(("CISCO-UBE-MIB", "ciscoUbeMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCubeMIBCompliance = ciscoCubeMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoCubeMIBCompliance.setDescription('The compliance statement for Cisco Unified Border Element (CUBE) MIB.')
ciscoUbeMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 2, 1)).setObjects(("CISCO-UBE-MIB", "cubeEnabled"), ("CISCO-UBE-MIB", "cubeVersion"), ("CISCO-UBE-MIB", "cubeTotalSessionAllowed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUbeMIBGroup = ciscoUbeMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoUbeMIBGroup.setDescription('A collection of objects which provides the capabilities of the CUBE feature.')
mibBuilder.exportSymbols("CISCO-UBE-MIB", ciscoUbeMIBGroups=ciscoUbeMIBGroups, cubeVersion=cubeVersion, ciscoUbeMIBConform=ciscoUbeMIBConform, ciscoUbeMIBCompliances=ciscoUbeMIBCompliances, PYSNMP_MODULE_ID=ciscoUbeMIB, cubeTotalSessionAllowed=cubeTotalSessionAllowed, ciscoCubeMIBCompliance=ciscoCubeMIBCompliance, ciscoUbeMIB=ciscoUbeMIB, ciscoUbeMIBGroup=ciscoUbeMIBGroup, ciscoUbeMIBObjects=ciscoUbeMIBObjects, cubeEnabled=cubeEnabled)
