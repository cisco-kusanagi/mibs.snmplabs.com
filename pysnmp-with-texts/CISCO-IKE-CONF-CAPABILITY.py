#
# PySNMP MIB module CISCO-IKE-CONF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IKE-CONF-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:01:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, TimeTicks, IpAddress, MibIdentifier, ModuleIdentity, Unsigned32, Counter32, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "TimeTicks", "IpAddress", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Counter32", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCicIkeCfgCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 489))
ciscoCicIkeCfgCapability.setRevisions(('2006-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCicIkeCfgCapability.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoCicIkeCfgCapability.setLastUpdated('200602020000Z')
if mibBuilder.loadTexts: ciscoCicIkeCfgCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCicIkeCfgCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoCicIkeCfgCapability.setDescription('Agent capabilities for CISCO-IKE-CONFIGURATION-MIB')
cCicIkeCfgCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 489, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCicIkeCfgCapSanOSV30R1MDS9000 = cCicIkeCfgCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCicIkeCfgCapSanOSV30R1MDS9000 = cCicIkeCfgCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: cCicIkeCfgCapSanOSV30R1MDS9000.setDescription('Cisco IKE Configuration MIB capabilities')
mibBuilder.exportSymbols("CISCO-IKE-CONF-CAPABILITY", ciscoCicIkeCfgCapability=ciscoCicIkeCfgCapability, PYSNMP_MODULE_ID=ciscoCicIkeCfgCapability, cCicIkeCfgCapSanOSV30R1MDS9000=cCicIkeCfgCapSanOSV30R1MDS9000)
