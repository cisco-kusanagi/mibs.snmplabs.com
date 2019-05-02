#
# PySNMP MIB module CISCO-CASA-FA-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CASA-FA-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:52:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
iso, ModuleIdentity, Gauge32, IpAddress, MibIdentifier, Integer32, TimeTicks, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Gauge32", "IpAddress", "MibIdentifier", "Integer32", "TimeTicks", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Bits", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCasaFaCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 135))
ciscoCasaFaCapability.setRevisions(('2000-12-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCasaFaCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCasaFaCapability.setLastUpdated('200012010000Z')
if mibBuilder.loadTexts: ciscoCasaFaCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCasaFaCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoCasaFaCapability.setDescription('Agent capabilities for the CASA-FA-MIB')
ciscoCasaFaCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 135, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasaFaCapabilityV12R01 = ciscoCasaFaCapabilityV12R01.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasaFaCapabilityV12R01 = ciscoCasaFaCapabilityV12R01.setStatus('current')
if mibBuilder.loadTexts: ciscoCasaFaCapabilityV12R01.setDescription('IOS 12.1 Cisco Casa Forwarding Agent MIB capabilities')
mibBuilder.exportSymbols("CISCO-CASA-FA-CAPABILITY", ciscoCasaFaCapabilityV12R01=ciscoCasaFaCapabilityV12R01, ciscoCasaFaCapability=ciscoCasaFaCapability, PYSNMP_MODULE_ID=ciscoCasaFaCapability)
