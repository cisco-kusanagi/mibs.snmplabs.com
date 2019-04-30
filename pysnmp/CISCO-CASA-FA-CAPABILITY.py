#
# PySNMP MIB module CISCO-CASA-FA-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CASA-FA-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:35:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, ObjectIdentity, iso, Unsigned32, Counter32, IpAddress, Gauge32, Integer32, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "ObjectIdentity", "iso", "Unsigned32", "Counter32", "IpAddress", "Gauge32", "Integer32", "Counter64", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCasaFaCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 135))
ciscoCasaFaCapability.setRevisions(('2000-12-01 00:00',))
if mibBuilder.loadTexts: ciscoCasaFaCapability.setLastUpdated('200012010000Z')
if mibBuilder.loadTexts: ciscoCasaFaCapability.setOrganization('Cisco Systems, Inc.')
ciscoCasaFaCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 135, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasaFaCapabilityV12R01 = ciscoCasaFaCapabilityV12R01.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasaFaCapabilityV12R01 = ciscoCasaFaCapabilityV12R01.setStatus('current')
mibBuilder.exportSymbols("CISCO-CASA-FA-CAPABILITY", ciscoCasaFaCapabilityV12R01=ciscoCasaFaCapabilityV12R01, PYSNMP_MODULE_ID=ciscoCasaFaCapability, ciscoCasaFaCapability=ciscoCasaFaCapability)
