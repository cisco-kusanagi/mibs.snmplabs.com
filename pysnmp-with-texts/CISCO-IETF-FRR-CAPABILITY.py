#
# PySNMP MIB module CISCO-IETF-FRR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-FRR-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:00:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
NotificationType, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, IpAddress, Integer32, Counter64, Counter32, Unsigned32, Gauge32, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "IpAddress", "Integer32", "Counter64", "Counter32", "Unsigned32", "Gauge32", "ModuleIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIetfFrrCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 310))
ciscoIetfFrrCapability.setRevisions(('2003-05-23 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIetfFrrCapability.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: ciscoIetfFrrCapability.setLastUpdated('200305231200Z')
if mibBuilder.loadTexts: ciscoIetfFrrCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfFrrCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: mpls-mib@cisco.com')
if mibBuilder.loadTexts: ciscoIetfFrrCapability.setDescription('Agent capabilities for CISCO-IETF-FRR-MIB')
ciscoIetfFrrCapabilityV12R0026S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 310, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfFrrCapabilityV12R0026S = ciscoIetfFrrCapabilityV12R0026S.setProductRelease('Cisco IOS 12.0(26)S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfFrrCapabilityV12R0026S = ciscoIetfFrrCapabilityV12R0026S.setStatus('current')
if mibBuilder.loadTexts: ciscoIetfFrrCapabilityV12R0026S.setDescription('MPLS Traffic Engineering Fast Reroute MIB capabilities')
mibBuilder.exportSymbols("CISCO-IETF-FRR-CAPABILITY", ciscoIetfFrrCapability=ciscoIetfFrrCapability, ciscoIetfFrrCapabilityV12R0026S=ciscoIetfFrrCapabilityV12R0026S, PYSNMP_MODULE_ID=ciscoIetfFrrCapability)
