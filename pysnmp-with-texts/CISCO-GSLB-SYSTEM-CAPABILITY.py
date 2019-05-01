#
# PySNMP MIB module CISCO-GSLB-SYSTEM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-GSLB-SYSTEM-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:59:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
IpAddress, MibIdentifier, Bits, ModuleIdentity, TimeTicks, ObjectIdentity, Counter64, NotificationType, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Bits", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Counter64", "NotificationType", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGslbSystemCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 534))
ciscoGslbSystemCapability.setRevisions(('2011-09-14 00:00', '2008-09-15 00:00', '2007-02-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGslbSystemCapability.setRevisionsDescriptions(('Added ciscoGslbSystemCapabilityV04R01 agent capabilities for Global Site Selector(GSS) release 4.1.0.', 'Added ciscoGslbSystemCapabilityV03R00 agent capabilities for Global Site Selector(GSS) release 3.0.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGslbSystemCapability.setLastUpdated('201109140000Z')
if mibBuilder.loadTexts: ciscoGslbSystemCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGslbSystemCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-slb@cisco.com')
if mibBuilder.loadTexts: ciscoGslbSystemCapability.setDescription('The capabilities description of CISCO-GSLB-SYSTEM-MIB.')
ciscoGslbSystemCapabilityV02R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 534, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV02R00 = ciscoGslbSystemCapabilityV02R00.setProductRelease('GSS 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV02R00 = ciscoGslbSystemCapabilityV02R00.setStatus('current')
if mibBuilder.loadTexts: ciscoGslbSystemCapabilityV02R00.setDescription('GSS 2.0 Cisco GSLB SYSTEM MIB capabilities')
ciscoGslbSystemCapabilityV03R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 534, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV03R00 = ciscoGslbSystemCapabilityV03R00.setProductRelease('Global Site Selector(GSS) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV03R00 = ciscoGslbSystemCapabilityV03R00.setStatus('current')
if mibBuilder.loadTexts: ciscoGslbSystemCapabilityV03R00.setDescription('GSS 3.0 Cisco GSLB SYSTEM MIB capabilities')
ciscoGslbSystemCapabilityV04R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 534, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV04R01 = ciscoGslbSystemCapabilityV04R01.setProductRelease('Global Site Selector(GSS) 4.1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV04R01 = ciscoGslbSystemCapabilityV04R01.setStatus('current')
if mibBuilder.loadTexts: ciscoGslbSystemCapabilityV04R01.setDescription('GSS 4.1.0 Cisco GSLB SYSTEM MIB capabilities')
mibBuilder.exportSymbols("CISCO-GSLB-SYSTEM-CAPABILITY", PYSNMP_MODULE_ID=ciscoGslbSystemCapability, ciscoGslbSystemCapabilityV04R01=ciscoGslbSystemCapabilityV04R01, ciscoGslbSystemCapability=ciscoGslbSystemCapability, ciscoGslbSystemCapabilityV02R00=ciscoGslbSystemCapabilityV02R00, ciscoGslbSystemCapabilityV03R00=ciscoGslbSystemCapabilityV03R00)
