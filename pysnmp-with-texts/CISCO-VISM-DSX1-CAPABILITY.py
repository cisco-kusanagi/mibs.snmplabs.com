#
# PySNMP MIB module CISCO-VISM-DSX1-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VISM-DSX1-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:18:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
TimeTicks, NotificationType, iso, IpAddress, Counter64, Gauge32, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, ObjectIdentity, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "iso", "IpAddress", "Counter64", "Gauge32", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "ObjectIdentity", "Unsigned32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVismDsx1Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 450))
ciscoVismDsx1Capability.setRevisions(('2005-09-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVismDsx1Capability.setRevisionsDescriptions(('Initial version of this capability file.',))
if mibBuilder.loadTexts: ciscoVismDsx1Capability.setLastUpdated('200509260000Z')
if mibBuilder.loadTexts: ciscoVismDsx1Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVismDsx1Capability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoVismDsx1Capability.setDescription('Agent capabilities for CISCO-VISM-DSX1-MIB.')
cVismDsx1CapabilityV3325 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 450, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismDsx1CapabilityV3325 = cVismDsx1CapabilityV3325.setProductRelease('Cisco VISM Release 3.3.25')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismDsx1CapabilityV3325 = cVismDsx1CapabilityV3325.setStatus('current')
if mibBuilder.loadTexts: cVismDsx1CapabilityV3325.setDescription('CISCO-VISM-DSX1-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VISM-DSX1-CAPABILITY", ciscoVismDsx1Capability=ciscoVismDsx1Capability, PYSNMP_MODULE_ID=ciscoVismDsx1Capability, cVismDsx1CapabilityV3325=cVismDsx1CapabilityV3325)
