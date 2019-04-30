#
# PySNMP MIB module CISCO-IPSEC-PROV-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IPSEC-PROV-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:45:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Unsigned32, NotificationType, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, ModuleIdentity, Bits, iso, Gauge32, MibIdentifier, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Bits", "iso", "Gauge32", "MibIdentifier", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIPsecProvCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 486))
ciscoIPsecProvCapability.setRevisions(('2006-02-02 00:00',))
if mibBuilder.loadTexts: ciscoIPsecProvCapability.setLastUpdated('200602020000Z')
if mibBuilder.loadTexts: ciscoIPsecProvCapability.setOrganization('Cisco Systems, Inc.')
cIPsecProvCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 486, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIPsecProvCapSanOSV30R1MDS9000 = cIPsecProvCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIPsecProvCapSanOSV30R1MDS9000 = cIPsecProvCapSanOSV30R1MDS9000.setStatus('current')
mibBuilder.exportSymbols("CISCO-IPSEC-PROV-CAPABILITY", PYSNMP_MODULE_ID=ciscoIPsecProvCapability, cIPsecProvCapSanOSV30R1MDS9000=cIPsecProvCapSanOSV30R1MDS9000, ciscoIPsecProvCapability=ciscoIPsecProvCapability)
