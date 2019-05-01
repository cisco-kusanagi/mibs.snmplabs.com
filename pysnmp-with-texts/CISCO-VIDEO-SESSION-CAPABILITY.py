#
# PySNMP MIB module CISCO-VIDEO-SESSION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VIDEO-SESSION-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:18:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Counter64, Gauge32, MibIdentifier, Counter32, Unsigned32, iso, TimeTicks, NotificationType, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Counter64", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "iso", "TimeTicks", "NotificationType", "Integer32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVideoSessionCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 599))
ciscoVideoSessionCapability.setRevisions(('2011-05-24 00:00', '2010-11-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVideoSessionCapability.setRevisionsDescriptions(('Added ciscoVideoSessionCapabilityV152T02.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVideoSessionCapability.setLastUpdated('201105240000Z')
if mibBuilder.loadTexts: ciscoVideoSessionCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVideoSessionCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-video@cisco.com')
if mibBuilder.loadTexts: ciscoVideoSessionCapability.setDescription('Agent capabilities for CISCO-VIDEO-SESSION-MIB.')
ciscoVideoSessionCapabilityV15R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 599, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVideoSessionCapabilityV15R01 = ciscoVideoSessionCapabilityV15R01.setProductRelease('OS=IOS\n                     OSVERSION=15.1\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVideoSessionCapabilityV15R01 = ciscoVideoSessionCapabilityV15R01.setStatus('current')
if mibBuilder.loadTexts: ciscoVideoSessionCapabilityV15R01.setDescription('Cisco Video Session MIB capabilities.')
ciscoVideoSessionCapabilityV152T02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 599, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVideoSessionCapabilityV152T02 = ciscoVideoSessionCapabilityV152T02.setProductRelease('OS=IOS\n                     OSVERSION=15.2(2)T\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVideoSessionCapabilityV152T02 = ciscoVideoSessionCapabilityV152T02.setStatus('current')
if mibBuilder.loadTexts: ciscoVideoSessionCapabilityV152T02.setDescription('Cisco Video Session MIB capabilities. Some objects are not implemented due to DSP statistics reporting capabilities.')
mibBuilder.exportSymbols("CISCO-VIDEO-SESSION-CAPABILITY", ciscoVideoSessionCapability=ciscoVideoSessionCapability, ciscoVideoSessionCapabilityV152T02=ciscoVideoSessionCapabilityV152T02, ciscoVideoSessionCapabilityV15R01=ciscoVideoSessionCapabilityV15R01, PYSNMP_MODULE_ID=ciscoVideoSessionCapability)
