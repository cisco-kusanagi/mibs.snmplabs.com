#
# PySNMP MIB module CISCO-SYS-INFO-LOG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SYS-INFO-LOG-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:57:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Unsigned32, NotificationType, Counter64, ObjectIdentity, iso, ModuleIdentity, TimeTicks, Integer32, Bits, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "Counter64", "ObjectIdentity", "iso", "ModuleIdentity", "TimeTicks", "Integer32", "Bits", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSysInfoLogCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 321))
ciscoSysInfoLogCapability.setRevisions(('2005-08-24 00:00', '2003-08-01 00:00',))
if mibBuilder.loadTexts: ciscoSysInfoLogCapability.setLastUpdated('200508240000Z')
if mibBuilder.loadTexts: ciscoSysInfoLogCapability.setOrganization('Cisco Systems, Inc.')
ciscoSysInfoLogCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 321, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogCapCatOSV08R0101 = ciscoSysInfoLogCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogCapCatOSV08R0101 = ciscoSysInfoLogCapCatOSV08R0101.setStatus('current')
ciscoSysInfoLogCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 321, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogCapCatOSV08R0501 = ciscoSysInfoLogCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogCapCatOSV08R0501 = ciscoSysInfoLogCapCatOSV08R0501.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYS-INFO-LOG-CAPABILITY", ciscoSysInfoLogCapCatOSV08R0101=ciscoSysInfoLogCapCatOSV08R0101, ciscoSysInfoLogCapCatOSV08R0501=ciscoSysInfoLogCapCatOSV08R0501, ciscoSysInfoLogCapability=ciscoSysInfoLogCapability, PYSNMP_MODULE_ID=ciscoSysInfoLogCapability)
