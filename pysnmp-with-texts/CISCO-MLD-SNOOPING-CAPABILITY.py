#
# PySNMP MIB module CISCO-MLD-SNOOPING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MLD-SNOOPING-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:07:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Counter32, MibIdentifier, TimeTicks, Unsigned32, iso, NotificationType, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, Gauge32, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "TimeTicks", "Unsigned32", "iso", "NotificationType", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "Gauge32", "Counter64", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMldSnoopingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 586))
ciscoMldSnoopingCapability.setRevisions(('2010-03-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMldSnoopingCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMldSnoopingCapability.setLastUpdated('201003020000Z')
if mibBuilder.loadTexts: ciscoMldSnoopingCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMldSnoopingCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-<list>@cisco.com')
if mibBuilder.loadTexts: ciscoMldSnoopingCapability.setDescription('The capabilities description of CISCO-MLD-SNOOPING-MIB.')
ciscoMldSnoopingCapabilityV04R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 586, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMldSnoopingCapabilityV04R01 = ciscoMldSnoopingCapabilityV04R01.setProductRelease('Cisco IOS-XR')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMldSnoopingCapabilityV04R01 = ciscoMldSnoopingCapabilityV04R01.setStatus('current')
if mibBuilder.loadTexts: ciscoMldSnoopingCapabilityV04R01.setDescription('Capabilities description for CISCO-MLD-SNOOPING-MIB.')
mibBuilder.exportSymbols("CISCO-MLD-SNOOPING-CAPABILITY", ciscoMldSnoopingCapability=ciscoMldSnoopingCapability, PYSNMP_MODULE_ID=ciscoMldSnoopingCapability, ciscoMldSnoopingCapabilityV04R01=ciscoMldSnoopingCapabilityV04R01)
