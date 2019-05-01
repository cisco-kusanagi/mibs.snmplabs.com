#
# PySNMP MIB module CISCO-SVI-AUTOSTATE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SVI-AUTOSTATE-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:13:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
IpAddress, ObjectIdentity, MibIdentifier, Bits, TimeTicks, NotificationType, ModuleIdentity, Counter32, Integer32, iso, Gauge32, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "MibIdentifier", "Bits", "TimeTicks", "NotificationType", "ModuleIdentity", "Counter32", "Integer32", "iso", "Gauge32", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoSVIAutostateCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 384))
ciscoSVIAutostateCapability.setRevisions(('2004-04-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSVIAutostateCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSVIAutostateCapability.setLastUpdated('200404080000Z')
if mibBuilder.loadTexts: ciscoSVIAutostateCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSVIAutostateCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSVIAutostateCapability.setDescription('The capabilities description of CISCO-SVI-AUTOSTATE-MIB.')
csaCapabilityCatOSV08R0301Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 384, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaCapabilityCatOSV08R0301Cat6k = csaCapabilityCatOSV08R0301Cat6k.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaCapabilityCatOSV08R0301Cat6k = csaCapabilityCatOSV08R0301Cat6k.setStatus('current')
if mibBuilder.loadTexts: csaCapabilityCatOSV08R0301Cat6k.setDescription('CISCO-SVI-AUTOSTATE-MIB capabilities.')
csaCapabilityV12R0218SXDCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 384, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaCapabilityV12R0218SXDCat6k = csaCapabilityV12R0218SXDCat6k.setProductRelease('Cisco IOS 12.2(18)SXD on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaCapabilityV12R0218SXDCat6k = csaCapabilityV12R0218SXDCat6k.setStatus('current')
if mibBuilder.loadTexts: csaCapabilityV12R0218SXDCat6k.setDescription('CISCO-SVI-AUTOSTATE-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SVI-AUTOSTATE-CAPABILITY", PYSNMP_MODULE_ID=ciscoSVIAutostateCapability, csaCapabilityV12R0218SXDCat6k=csaCapabilityV12R0218SXDCat6k, csaCapabilityCatOSV08R0301Cat6k=csaCapabilityCatOSV08R0301Cat6k, ciscoSVIAutostateCapability=ciscoSVIAutostateCapability)
