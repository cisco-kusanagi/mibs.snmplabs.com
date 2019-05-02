#
# PySNMP MIB module CISCO-CAS-IF-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CAS-IF-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:52:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, iso, Integer32, Bits, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Counter32, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "iso", "Integer32", "Bits", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Counter32", "TimeTicks", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCasIfExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 349))
ciscoCasIfExtCapability.setRevisions(('2004-01-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCasIfExtCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCasIfExtCapability.setLastUpdated('200401190000Z')
if mibBuilder.loadTexts: ciscoCasIfExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCasIfExtCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoCasIfExtCapability.setDescription('The agent capabilities for CISCO-CAS-IF-EXT-MIB.')
ciscoCasIfExtCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 349, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfExtCapabilityV5R00 = ciscoCasIfExtCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfExtCapabilityV5R00 = ciscoCasIfExtCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoCasIfExtCapabilityV5R00.setDescription('CISCO-CAS-IF-EXT-MIB capabilities for Voice Switch Service Module(VXSM) in Release 5.0.0.')
mibBuilder.exportSymbols("CISCO-CAS-IF-EXT-CAPABILITY", ciscoCasIfExtCapabilityV5R00=ciscoCasIfExtCapabilityV5R00, ciscoCasIfExtCapability=ciscoCasIfExtCapability, PYSNMP_MODULE_ID=ciscoCasIfExtCapability)
