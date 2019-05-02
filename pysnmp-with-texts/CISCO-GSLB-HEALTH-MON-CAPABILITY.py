#
# PySNMP MIB module CISCO-GSLB-HEALTH-MON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-GSLB-HEALTH-MON-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:59:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, TimeTicks, ModuleIdentity, iso, Counter32, NotificationType, MibIdentifier, Gauge32, ObjectIdentity, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "TimeTicks", "ModuleIdentity", "iso", "Counter32", "NotificationType", "MibIdentifier", "Gauge32", "ObjectIdentity", "Counter64", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoGslbHealthMonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 536))
ciscoGslbHealthMonCapability.setRevisions(('2007-02-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGslbHealthMonCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGslbHealthMonCapability.setLastUpdated('200702230000Z')
if mibBuilder.loadTexts: ciscoGslbHealthMonCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGslbHealthMonCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-slb@cisco.com')
if mibBuilder.loadTexts: ciscoGslbHealthMonCapability.setDescription('The capabilities description of CISCO-GSLB-HEALTH-MON-MIB.')
ciscoGslbHealthMonCapabilityV02R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 536, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbHealthMonCapabilityV02R00 = ciscoGslbHealthMonCapabilityV02R00.setProductRelease('GSS 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbHealthMonCapabilityV02R00 = ciscoGslbHealthMonCapabilityV02R00.setStatus('current')
if mibBuilder.loadTexts: ciscoGslbHealthMonCapabilityV02R00.setDescription('GSS 2.0 Cisco GSLB HEALTH MON MIB capabilities')
mibBuilder.exportSymbols("CISCO-GSLB-HEALTH-MON-CAPABILITY", PYSNMP_MODULE_ID=ciscoGslbHealthMonCapability, ciscoGslbHealthMonCapability=ciscoGslbHealthMonCapability, ciscoGslbHealthMonCapabilityV02R00=ciscoGslbHealthMonCapabilityV02R00)
