#
# PySNMP MIB module CISCO-ITP-MSU-RATES-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-MSU-RATES-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:03:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
ObjectIdentity, MibIdentifier, iso, NotificationType, ModuleIdentity, Counter32, Bits, Unsigned32, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "iso", "NotificationType", "ModuleIdentity", "Counter32", "Bits", "Unsigned32", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoItpMsuRatesCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 537))
ciscoItpMsuRatesCapability.setRevisions(('2007-03-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpMsuRatesCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpMsuRatesCapability.setLastUpdated('200703200000Z')
if mibBuilder.loadTexts: ciscoItpMsuRatesCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpMsuRatesCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-itp@cisco.com')
if mibBuilder.loadTexts: ciscoItpMsuRatesCapability.setDescription('Agent capabilities for the CISCO-ITP-MSU-RATES-MIB.')
ciscoItpMsuCapabilityV12R0225SW7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 537, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0225SW7 = ciscoItpMsuCapabilityV12R0225SW7.setProductRelease('Cisco IOS 12.2(25)SW7')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0225SW7 = ciscoItpMsuCapabilityV12R0225SW7.setStatus('current')
if mibBuilder.loadTexts: ciscoItpMsuCapabilityV12R0225SW7.setDescription('Cisco IOS 12.2(25)SW7 CISCO-ITP-MSU-RATES-MIB.my User Agent MIB capabilities.')
ciscoItpMsuCapabilityV12R0218IXB = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 537, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0218IXB = ciscoItpMsuCapabilityV12R0218IXB.setProductRelease('Cisco IOS 12.2(18)IXB')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0218IXB = ciscoItpMsuCapabilityV12R0218IXB.setStatus('current')
if mibBuilder.loadTexts: ciscoItpMsuCapabilityV12R0218IXB.setDescription('Cisco IOS 12.2(18)IXB CISCO-ITP-MSU-RATES-MIB.my User Agent MIB capabilities.')
ciscoItpMsuCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 537, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0411SW = ciscoItpMsuCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0411SW = ciscoItpMsuCapabilityV12R0411SW.setStatus('current')
if mibBuilder.loadTexts: ciscoItpMsuCapabilityV12R0411SW.setDescription('Cisco IOS 12.4(11)SW CISCO-ITP-MSU-RATES-MIB.my User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-MSU-RATES-CAPABILITY", ciscoItpMsuCapabilityV12R0411SW=ciscoItpMsuCapabilityV12R0411SW, ciscoItpMsuCapabilityV12R0225SW7=ciscoItpMsuCapabilityV12R0225SW7, ciscoItpMsuRatesCapability=ciscoItpMsuRatesCapability, PYSNMP_MODULE_ID=ciscoItpMsuRatesCapability, ciscoItpMsuCapabilityV12R0218IXB=ciscoItpMsuCapabilityV12R0218IXB)
