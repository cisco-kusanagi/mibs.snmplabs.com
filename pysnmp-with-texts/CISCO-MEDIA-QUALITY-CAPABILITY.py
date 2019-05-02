#
# PySNMP MIB module CISCO-MEDIA-QUALITY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MEDIA-QUALITY-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:07:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, NotificationType, TimeTicks, MibIdentifier, ObjectIdentity, iso, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "NotificationType", "TimeTicks", "MibIdentifier", "ObjectIdentity", "iso", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMediaQualityCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 604))
ciscoMediaQualityCapability.setRevisions(('2011-09-23 00:00', '2011-04-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMediaQualityCapability.setRevisionsDescriptions(("Added agent capabilities 'ciscoMediaQualityCapabilityV152R02' for IOS 15.2(2)T.", 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMediaQualityCapability.setLastUpdated('201109230000Z')
if mibBuilder.loadTexts: ciscoMediaQualityCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMediaQualityCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice@cisco.com')
if mibBuilder.loadTexts: ciscoMediaQualityCapability.setDescription('Agent capabilities for CISCO-MEDIA-QUALITY-MIB.')
ciscoMediaQualityCapabilityV152R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 604, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMediaQualityCapabilityV152R01 = ciscoMediaQualityCapabilityV152R01.setProductRelease('OS=IOS\n                     OSVERSION=15.2(1)T\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMediaQualityCapabilityV152R01 = ciscoMediaQualityCapabilityV152R01.setStatus('current')
if mibBuilder.loadTexts: ciscoMediaQualityCapabilityV152R01.setDescription('Agent capabilities for CISCO-MEDIA-QUALITY-MIB release in 15.2(1)T.')
ciscoMediaQualityCapabilityV152R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 604, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMediaQualityCapabilityV152R02 = ciscoMediaQualityCapabilityV152R02.setProductRelease('OS=IOS\n                     OSVERSION=15.2(2)T\n                     PLATFORM=c28xx,c3825,c3845,c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMediaQualityCapabilityV152R02 = ciscoMediaQualityCapabilityV152R02.setStatus('current')
if mibBuilder.loadTexts: ciscoMediaQualityCapabilityV152R02.setDescription('Agent capabilities for CISCO-MEDIA-QUALITY-MIB release 15.2(2)T.')
mibBuilder.exportSymbols("CISCO-MEDIA-QUALITY-CAPABILITY", ciscoMediaQualityCapabilityV152R02=ciscoMediaQualityCapabilityV152R02, ciscoMediaQualityCapabilityV152R01=ciscoMediaQualityCapabilityV152R01, PYSNMP_MODULE_ID=ciscoMediaQualityCapability, ciscoMediaQualityCapability=ciscoMediaQualityCapability)
