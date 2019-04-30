#
# PySNMP MIB module CISCO-SECURE-SHELL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SECURE-SHELL-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:54:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
NotificationType, MibIdentifier, ModuleIdentity, Bits, IpAddress, Counter64, ObjectIdentity, iso, Integer32, Unsigned32, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "ModuleIdentity", "Bits", "IpAddress", "Counter64", "ObjectIdentity", "iso", "Integer32", "Unsigned32", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
ciscoSecureShellCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoSecureShellCapability.setRevisions(('2004-04-19 00:00',))
if mibBuilder.loadTexts: ciscoSecureShellCapability.setLastUpdated('200404190000Z')
if mibBuilder.loadTexts: ciscoSecureShellCapability.setOrganization('Cisco Systems, Inc.')
cSecureShellCapCatOSV08R0401k9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSecureShellCapCatOSV08R0401k9 = cSecureShellCapCatOSV08R0401k9.setProductRelease('Cisco CatOS 8.4(1) cryptographic\n                         software with Secure Shell support.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSecureShellCapCatOSV08R0401k9 = cSecureShellCapCatOSV08R0401k9.setStatus('current')
mibBuilder.exportSymbols("CISCO-SECURE-SHELL-CAPABILITY", PYSNMP_MODULE_ID=ciscoSecureShellCapability, cSecureShellCapCatOSV08R0401k9=cSecureShellCapCatOSV08R0401k9, ciscoSecureShellCapability=ciscoSecureShellCapability)
