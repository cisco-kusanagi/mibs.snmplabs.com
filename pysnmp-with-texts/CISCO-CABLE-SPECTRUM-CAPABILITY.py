#
# PySNMP MIB module CISCO-CABLE-SPECTRUM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CABLE-SPECTRUM-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:51:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
TimeTicks, NotificationType, ModuleIdentity, Bits, Integer32, IpAddress, Counter32, Unsigned32, ObjectIdentity, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "ModuleIdentity", "Bits", "Integer32", "IpAddress", "Counter32", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCableSpectrumCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoCableSpectrumCapability.setRevisions(('2002-12-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCableSpectrumCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCableSpectrumCapability.setLastUpdated('200212180000Z')
if mibBuilder.loadTexts: ciscoCableSpectrumCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCableSpectrumCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ubr@cisco.com')
if mibBuilder.loadTexts: ciscoCableSpectrumCapability.setDescription('Agent capabilities for CISCO-CABLE-SPECTRUM-MIB')
ciscoCableSpectrumCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableSpectrumCapabilityV12R00 = ciscoCableSpectrumCapabilityV12R00.setProductRelease('Cisco IOS 12.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableSpectrumCapabilityV12R00 = ciscoCableSpectrumCapabilityV12R00.setStatus('current')
if mibBuilder.loadTexts: ciscoCableSpectrumCapabilityV12R00.setDescription('Cisco Cable Spectrum Management MIB capabilities.')
ciscoCableSpectrumCapabilityV12R01Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableSpectrumCapabilityV12R01Rev1 = ciscoCableSpectrumCapabilityV12R01Rev1.setProductRelease('Cisco IOS 12.1(05)EC and 12.2 BC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableSpectrumCapabilityV12R01Rev1 = ciscoCableSpectrumCapabilityV12R01Rev1.setStatus('current')
if mibBuilder.loadTexts: ciscoCableSpectrumCapabilityV12R01Rev1.setDescription('Cisco Cable Spectrum Management MIB capabilities.')
mibBuilder.exportSymbols("CISCO-CABLE-SPECTRUM-CAPABILITY", PYSNMP_MODULE_ID=ciscoCableSpectrumCapability, ciscoCableSpectrumCapability=ciscoCableSpectrumCapability, ciscoCableSpectrumCapabilityV12R01Rev1=ciscoCableSpectrumCapabilityV12R01Rev1, ciscoCableSpectrumCapabilityV12R00=ciscoCableSpectrumCapabilityV12R00)
