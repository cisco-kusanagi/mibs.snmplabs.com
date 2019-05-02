#
# PySNMP MIB module CISCO-SYS-INFO-LOG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SYS-INFO-LOG-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:13:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, TimeTicks, Gauge32, MibIdentifier, Counter64, ModuleIdentity, iso, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "TimeTicks", "Gauge32", "MibIdentifier", "Counter64", "ModuleIdentity", "iso", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSysInfoLogCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 321))
ciscoSysInfoLogCapability.setRevisions(('2005-08-24 00:00', '2003-08-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSysInfoLogCapability.setRevisionsDescriptions(('Added capability statement ciscoSysInfoLogCapCatOSV08R0501. Added VARIATION for csilServerProtocol in capability statement ciscoSysInfoLogCapCatOSV08R0101.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSysInfoLogCapability.setLastUpdated('200508240000Z')
if mibBuilder.loadTexts: ciscoSysInfoLogCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSysInfoLogCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSysInfoLogCapability.setDescription('The capabilities description of CISCO-SYS-INFO-LOG-MIB.')
ciscoSysInfoLogCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 321, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogCapCatOSV08R0101 = ciscoSysInfoLogCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogCapCatOSV08R0101 = ciscoSysInfoLogCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoSysInfoLogCapCatOSV08R0101.setDescription('CISCO-SYS-INFO-LOG-MIB capabilities.')
ciscoSysInfoLogCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 321, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogCapCatOSV08R0501 = ciscoSysInfoLogCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogCapCatOSV08R0501 = ciscoSysInfoLogCapCatOSV08R0501.setStatus('current')
if mibBuilder.loadTexts: ciscoSysInfoLogCapCatOSV08R0501.setDescription('CISCO-SYS-INFO-LOG-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SYS-INFO-LOG-CAPABILITY", PYSNMP_MODULE_ID=ciscoSysInfoLogCapability, ciscoSysInfoLogCapCatOSV08R0101=ciscoSysInfoLogCapCatOSV08R0101, ciscoSysInfoLogCapability=ciscoSysInfoLogCapability, ciscoSysInfoLogCapCatOSV08R0501=ciscoSysInfoLogCapCatOSV08R0501)
