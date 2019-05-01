#
# PySNMP MIB module CISCO-EVC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-EVC-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:57:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
iso, ModuleIdentity, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, Integer32, NotificationType, MibIdentifier, TimeTicks, Unsigned32, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "Integer32", "NotificationType", "MibIdentifier", "TimeTicks", "Unsigned32", "ObjectIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoEvcCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 568))
ciscoEvcCapability.setRevisions(('2008-08-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEvcCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEvcCapability.setLastUpdated('200808260000Z')
if mibBuilder.loadTexts: ciscoEvcCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEvcCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ethermibs@cisco.com')
if mibBuilder.loadTexts: ciscoEvcCapability.setDescription('Agent capabilities for the CISCO-EVC-MIB.')
ciscoEvcCapabilityV12R02SR = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 568, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEvcCapabilityV12R02SR = ciscoEvcCapabilityV12R02SR.setProductRelease('Cisco IOS 12.2 SR Release')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEvcCapabilityV12R02SR = ciscoEvcCapabilityV12R02SR.setStatus('current')
if mibBuilder.loadTexts: ciscoEvcCapabilityV12R02SR.setDescription('CISCO-EVC-MIB capabilities.')
ciscoEvcCapabilityV12R02XO = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 568, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEvcCapabilityV12R02XO = ciscoEvcCapabilityV12R02XO.setProductRelease('Cisco IOS 12.2 XO Release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEvcCapabilityV12R02XO = ciscoEvcCapabilityV12R02XO.setStatus('current')
if mibBuilder.loadTexts: ciscoEvcCapabilityV12R02XO.setDescription('CISCO-EVC-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-EVC-CAPABILITY", ciscoEvcCapability=ciscoEvcCapability, ciscoEvcCapabilityV12R02SR=ciscoEvcCapabilityV12R02SR, PYSNMP_MODULE_ID=ciscoEvcCapability, ciscoEvcCapabilityV12R02XO=ciscoEvcCapabilityV12R02XO)
