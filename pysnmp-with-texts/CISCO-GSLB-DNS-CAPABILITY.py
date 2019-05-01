#
# PySNMP MIB module CISCO-GSLB-DNS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-GSLB-DNS-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:59:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Gauge32, MibIdentifier, IpAddress, ObjectIdentity, Bits, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, iso, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "MibIdentifier", "IpAddress", "ObjectIdentity", "Bits", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "iso", "Counter32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGslbDnsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 535))
ciscoGslbDnsCapability.setRevisions(('2009-03-18 00:00', '2007-02-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGslbDnsCapability.setRevisionsDescriptions(('Added ciscoGslbDnsCapabilityV03R01 agent capabilities for Global Site Selector(GSS) release 3.1(0).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGslbDnsCapability.setLastUpdated('200903180000Z')
if mibBuilder.loadTexts: ciscoGslbDnsCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGslbDnsCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-slb@cisco.com')
if mibBuilder.loadTexts: ciscoGslbDnsCapability.setDescription('The capabilities description of CISCO-GSLB-DNS-MIB.')
ciscoGslbDnsCapabilityV02R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 535, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbDnsCapabilityV02R00 = ciscoGslbDnsCapabilityV02R00.setProductRelease('GSS 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbDnsCapabilityV02R00 = ciscoGslbDnsCapabilityV02R00.setStatus('current')
if mibBuilder.loadTexts: ciscoGslbDnsCapabilityV02R00.setDescription('GSS 2.0 Cisco GSLB DNS MIB capabilities')
ciscoGslbDnsCapabilityV03R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 535, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbDnsCapabilityV03R01 = ciscoGslbDnsCapabilityV03R01.setProductRelease('GSS 3.1(0)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbDnsCapabilityV03R01 = ciscoGslbDnsCapabilityV03R01.setStatus('current')
if mibBuilder.loadTexts: ciscoGslbDnsCapabilityV03R01.setDescription('GSS 3.1(0) Cisco GSLB DNS MIB capabilities')
mibBuilder.exportSymbols("CISCO-GSLB-DNS-CAPABILITY", ciscoGslbDnsCapabilityV02R00=ciscoGslbDnsCapabilityV02R00, ciscoGslbDnsCapabilityV03R01=ciscoGslbDnsCapabilityV03R01, PYSNMP_MODULE_ID=ciscoGslbDnsCapability, ciscoGslbDnsCapability=ciscoGslbDnsCapability)
