#
# PySNMP MIB module CISCO-IETF-PW-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-PW-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:00:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter64, Counter32, IpAddress, Integer32, ObjectIdentity, TimeTicks, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Gauge32, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "IpAddress", "Integer32", "ObjectIdentity", "TimeTicks", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Gauge32", "ModuleIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIetfPwCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 432))
ciscoIetfPwCapability.setRevisions(('2005-02-09 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIetfPwCapability.setRevisionsDescriptions(('Initial version: ciscoIetfPwCapabilityV12R00. ',))
if mibBuilder.loadTexts: ciscoIetfPwCapability.setLastUpdated('200502091200Z')
if mibBuilder.loadTexts: ciscoIetfPwCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfPwCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: mpls-mib@cisco.com')
if mibBuilder.loadTexts: ciscoIetfPwCapability.setDescription('Agent capabilities for CISCO-IETF-PW-MIB.')
ciscoIetfPwCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 432, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfPwCapabilityV12R00 = ciscoIetfPwCapabilityV12R00.setProductRelease('Cisco IOS 12.0(28)S, Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfPwCapabilityV12R00 = ciscoIetfPwCapabilityV12R00.setStatus('current')
if mibBuilder.loadTexts: ciscoIetfPwCapabilityV12R00.setDescription('Pseudowire MIB capabilities')
mibBuilder.exportSymbols("CISCO-IETF-PW-CAPABILITY", ciscoIetfPwCapability=ciscoIetfPwCapability, ciscoIetfPwCapabilityV12R00=ciscoIetfPwCapabilityV12R00, PYSNMP_MODULE_ID=ciscoIetfPwCapability)
