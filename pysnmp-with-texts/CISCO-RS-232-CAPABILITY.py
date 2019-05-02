#
# PySNMP MIB module CISCO-RS-232-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RS-232-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:10:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, NotificationType, IpAddress, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Gauge32, ObjectIdentity, Unsigned32, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "NotificationType", "IpAddress", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Gauge32", "ObjectIdentity", "Unsigned32", "Bits", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRS232Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 115))
ciscoRS232Capability.setRevisions(('2002-05-16 00:00', '1994-08-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRS232Capability.setRevisionsDescriptions(('Added ciscoRS232CapabilityV2R00 capability for MGX8850 and BPX SES products.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRS232Capability.setLastUpdated('200205160000Z')
if mibBuilder.loadTexts: ciscoRS232Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRS232Capability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoRS232Capability.setDescription('Agent capabilities for RS-232-MIB')
ciscoRS232CapabilityV10R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 115, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRS232CapabilityV10R02 = ciscoRS232CapabilityV10R02.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRS232CapabilityV10R02 = ciscoRS232CapabilityV10R02.setStatus('current')
if mibBuilder.loadTexts: ciscoRS232CapabilityV10R02.setDescription('IOS 10.2 rs232 mib capabilities')
ciscoRS232CapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 115, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRS232CapabilityV2R00 = ciscoRS232CapabilityV2R00.setProductRelease('MGX8850 Release 2.0,\n                BPX SES Release 1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRS232CapabilityV2R00 = ciscoRS232CapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoRS232CapabilityV2R00.setDescription('MGX8850 and BPX SES RS-232-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-RS-232-CAPABILITY", ciscoRS232Capability=ciscoRS232Capability, ciscoRS232CapabilityV2R00=ciscoRS232CapabilityV2R00, PYSNMP_MODULE_ID=ciscoRS232Capability, ciscoRS232CapabilityV10R02=ciscoRS232CapabilityV10R02)
