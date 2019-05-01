#
# PySNMP MIB module CISCO-TCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TCP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:14:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Counter64, Gauge32, ModuleIdentity, Bits, MibIdentifier, TimeTicks, Integer32, iso, IpAddress, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "ModuleIdentity", "Bits", "MibIdentifier", "TimeTicks", "Integer32", "iso", "IpAddress", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoTcpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 26))
ciscoTcpCapability.setRevisions(('2006-01-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTcpCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTcpCapability.setLastUpdated('200601180000Z')
if mibBuilder.loadTexts: ciscoTcpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTcpCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTcpCapability.setDescription('Agent capabilities for CISCO-TCP-MIB')
cTcpCapabilityIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 26, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cTcpCapabilityIOSXRV2R0CRS1 = cTcpCapabilityIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cTcpCapabilityIOSXRV2R0CRS1 = cTcpCapabilityIOSXRV2R0CRS1.setStatus('current')
if mibBuilder.loadTexts: cTcpCapabilityIOSXRV2R0CRS1.setDescription('CISCO-TCP-MIB capabilities for IOS XR release 2.0')
mibBuilder.exportSymbols("CISCO-TCP-CAPABILITY", PYSNMP_MODULE_ID=ciscoTcpCapability, cTcpCapabilityIOSXRV2R0CRS1=cTcpCapabilityIOSXRV2R0CRS1, ciscoTcpCapability=ciscoTcpCapability)
