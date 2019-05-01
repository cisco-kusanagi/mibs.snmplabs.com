#
# PySNMP MIB module ONS15501-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONS15501-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 14:34:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
synchronous, = mibBuilder.importSymbols("ONS15501-MIB", "synchronous")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Bits, ObjectIdentity, Integer32, TimeTicks, iso, Counter64, NotificationType, Counter32, Gauge32, IpAddress, Unsigned32, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "Integer32", "TimeTicks", "iso", "Counter64", "NotificationType", "Counter32", "Gauge32", "IpAddress", "Unsigned32", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ons15501MIBCapabilities = ModuleIdentity((1, 3, 6, 1, 4, 1, 1869, 15, 11))
ons15501MIBCapabilities.setRevisions(('2002-10-15 18:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ons15501MIBCapabilities.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: ons15501MIBCapabilities.setLastUpdated('200210151800Z')
if mibBuilder.loadTexts: ons15501MIBCapabilities.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ons15501MIBCapabilities.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-dwdm@cisco.com')
if mibBuilder.loadTexts: ons15501MIBCapabilities.setDescription('The MIB capability definition for ONS-15501 Optical Amplifier.')
synEmbLxCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 15))
ons15501CapOld = AgentCapabilities((1, 3, 6, 1, 4, 1, 1869, 15, 11, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapOld = ons15501CapOld.setProductRelease('Release 3.0 of ONS15501 software.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapOld = ons15501CapOld.setStatus('current')
if mibBuilder.loadTexts: ons15501CapOld.setDescription('The agent capability for ONS15501 release 3.0. The entity MIB is modeled as a single chassis containing 2 ports (input /output) and a power supply units. None of the parts are Field Replaceable Units (FRU). Main purpose of supporting the Entity MIB is for proper notification correlation.')
ons15501CapDC = AgentCapabilities((1, 3, 6, 1, 4, 1, 1869, 15, 11, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapDC = ons15501CapDC.setProductRelease('DC series of ONS15501, Release 4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapDC = ons15501CapDC.setStatus('current')
if mibBuilder.loadTexts: ons15501CapDC.setDescription('The agent capability for ONS15501 release 4.0 for DC series. The entity MIB is modeled as a single chassis containing 2 ports (input /output) and two power supply units. None of the parts are FRU. Main purpose of supporting the Entity MIB is for proper notification correlation.')
ons15501CapAC = AgentCapabilities((1, 3, 6, 1, 4, 1, 1869, 15, 11, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapAC = ons15501CapAC.setProductRelease('AC series of ONS15501, Release 4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapAC = ons15501CapAC.setStatus('current')
if mibBuilder.loadTexts: ons15501CapAC.setDescription('The agent capability for ONS15501 release 4.0 for AC series. The entity MIB is modeled as a single chassis containing 2 ports (input /output) and two power supply units. None of the parts are FRU. Main purpose of supporting the Entity MIB is for proper notification correlation.')
mibBuilder.exportSymbols("ONS15501-CAPABILITY", ons15501CapDC=ons15501CapDC, ons15501CapOld=ons15501CapOld, PYSNMP_MODULE_ID=ons15501MIBCapabilities, ons15501CapAC=ons15501CapAC, synEmbLxCapability=synEmbLxCapability, ons15501MIBCapabilities=ons15501MIBCapabilities)
