#
# PySNMP MIB module CISCO-IPSEC-SIGNALING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IPSEC-SIGNALING-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:45:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, IpAddress, Gauge32, Counter32, Unsigned32, MibIdentifier, NotificationType, Bits, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "IpAddress", "Gauge32", "Counter32", "Unsigned32", "MibIdentifier", "NotificationType", "Bits", "TimeTicks", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIPsecSigCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 488))
ciscoIPsecSigCapability.setRevisions(('2006-02-02 00:00',))
if mibBuilder.loadTexts: ciscoIPsecSigCapability.setLastUpdated('200602020000Z')
if mibBuilder.loadTexts: ciscoIPsecSigCapability.setOrganization('Cisco Systems, Inc.')
cIPsecSigCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 488, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIPsecSigCapSanOSV30R1MDS9000 = cIPsecSigCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIPsecSigCapSanOSV30R1MDS9000 = cIPsecSigCapSanOSV30R1MDS9000.setStatus('current')
mibBuilder.exportSymbols("CISCO-IPSEC-SIGNALING-CAPABILITY", cIPsecSigCapSanOSV30R1MDS9000=cIPsecSigCapSanOSV30R1MDS9000, PYSNMP_MODULE_ID=ciscoIPsecSigCapability, ciscoIPsecSigCapability=ciscoIPsecSigCapability)
