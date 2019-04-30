#
# PySNMP MIB module CISCO-ITP-MLR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-MLR-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:46:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Integer32, TimeTicks, Unsigned32, MibIdentifier, Counter64, ObjectIdentity, Gauge32, iso, NotificationType, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Unsigned32", "MibIdentifier", "Counter64", "ObjectIdentity", "Gauge32", "iso", "NotificationType", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoMlrCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 423))
ciscoMlrCapability.setRevisions(('2007-05-18 00:00', '2006-10-05 00:00', '2005-02-18 00:00', '2004-04-30 00:00',))
if mibBuilder.loadTexts: ciscoMlrCapability.setLastUpdated('200705180000Z')
if mibBuilder.loadTexts: ciscoMlrCapability.setOrganization('Cisco Systems, Inc.')
ciscoMlrCapabilityV12R0221SW01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 423, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0221SW01 = ciscoMlrCapabilityV12R0221SW01.setProductRelease('Cisco IOS 12.2(21)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0221SW01 = ciscoMlrCapabilityV12R0221SW01.setStatus('current')
ciscoMlrCapabilityV12R0225SW01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 423, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0225SW01 = ciscoMlrCapabilityV12R0225SW01.setProductRelease('Cisco IOS 12.2(25)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0225SW01 = ciscoMlrCapabilityV12R0225SW01.setStatus('current')
ciscoMlrCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 423, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0218IXA = ciscoMlrCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0218IXA = ciscoMlrCapabilityV12R0218IXA.setStatus('current')
ciscoMlrCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 423, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0411SW = ciscoMlrCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0411SW = ciscoMlrCapabilityV12R0411SW.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-MLR-CAPABILITY", ciscoMlrCapabilityV12R0221SW01=ciscoMlrCapabilityV12R0221SW01, ciscoMlrCapabilityV12R0218IXA=ciscoMlrCapabilityV12R0218IXA, ciscoMlrCapabilityV12R0225SW01=ciscoMlrCapabilityV12R0225SW01, PYSNMP_MODULE_ID=ciscoMlrCapability, ciscoMlrCapability=ciscoMlrCapability, ciscoMlrCapabilityV12R0411SW=ciscoMlrCapabilityV12R0411SW)
