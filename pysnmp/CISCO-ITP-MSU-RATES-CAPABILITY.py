#
# PySNMP MIB module CISCO-ITP-MSU-RATES-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-MSU-RATES-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:46:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Bits, Unsigned32, IpAddress, MibIdentifier, ModuleIdentity, Integer32, ObjectIdentity, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "IpAddress", "MibIdentifier", "ModuleIdentity", "Integer32", "ObjectIdentity", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "TimeTicks", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoItpMsuRatesCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 537))
ciscoItpMsuRatesCapability.setRevisions(('2007-03-20 00:00',))
if mibBuilder.loadTexts: ciscoItpMsuRatesCapability.setLastUpdated('200703200000Z')
if mibBuilder.loadTexts: ciscoItpMsuRatesCapability.setOrganization('Cisco Systems, Inc.')
ciscoItpMsuCapabilityV12R0225SW7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 537, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0225SW7 = ciscoItpMsuCapabilityV12R0225SW7.setProductRelease('Cisco IOS 12.2(25)SW7')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0225SW7 = ciscoItpMsuCapabilityV12R0225SW7.setStatus('current')
ciscoItpMsuCapabilityV12R0218IXB = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 537, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0218IXB = ciscoItpMsuCapabilityV12R0218IXB.setProductRelease('Cisco IOS 12.2(18)IXB')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0218IXB = ciscoItpMsuCapabilityV12R0218IXB.setStatus('current')
ciscoItpMsuCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 537, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0411SW = ciscoItpMsuCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0411SW = ciscoItpMsuCapabilityV12R0411SW.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-MSU-RATES-CAPABILITY", PYSNMP_MODULE_ID=ciscoItpMsuRatesCapability, ciscoItpMsuCapabilityV12R0225SW7=ciscoItpMsuCapabilityV12R0225SW7, ciscoItpMsuCapabilityV12R0411SW=ciscoItpMsuCapabilityV12R0411SW, ciscoItpMsuRatesCapability=ciscoItpMsuRatesCapability, ciscoItpMsuCapabilityV12R0218IXB=ciscoItpMsuCapabilityV12R0218IXB)
