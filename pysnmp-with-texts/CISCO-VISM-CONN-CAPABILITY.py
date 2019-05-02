#
# PySNMP MIB module CISCO-VISM-CONN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VISM-CONN-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:18:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
iso, ObjectIdentity, ModuleIdentity, TimeTicks, Integer32, Counter64, NotificationType, Counter32, IpAddress, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Integer32", "Counter64", "NotificationType", "Counter32", "IpAddress", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVismConnCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 400))
ciscoVismConnCapability.setRevisions(('2004-03-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVismConnCapability.setRevisionsDescriptions(('Initial version of this capability file.',))
if mibBuilder.loadTexts: ciscoVismConnCapability.setLastUpdated('200403170000Z')
if mibBuilder.loadTexts: ciscoVismConnCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVismConnCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoVismConnCapability.setDescription('The capabilities description of CISCO-VISM-CONN-MIB.')
cVismConnCapabilityV321 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 400, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismConnCapabilityV321 = cVismConnCapabilityV321.setProductRelease('Cisco VISM Release 3.2.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismConnCapabilityV321 = cVismConnCapabilityV321.setStatus('current')
if mibBuilder.loadTexts: cVismConnCapabilityV321.setDescription('CISCO-VISM-CONN-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VISM-CONN-CAPABILITY", cVismConnCapabilityV321=cVismConnCapabilityV321, PYSNMP_MODULE_ID=ciscoVismConnCapability, ciscoVismConnCapability=ciscoVismConnCapability)
