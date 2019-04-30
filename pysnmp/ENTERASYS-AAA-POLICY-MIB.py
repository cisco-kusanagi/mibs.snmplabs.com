#
# PySNMP MIB module ENTERASYS-AAA-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-AAA-POLICY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:48:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, TimeTicks, ObjectIdentity, NotificationType, MibIdentifier, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, IpAddress, iso, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "ObjectIdentity", "NotificationType", "MibIdentifier", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "IpAddress", "iso", "Bits", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysAAAPolicyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51))
etsysAAAPolicyMIB.setRevisions(('2004-07-29 19:06',))
if mibBuilder.loadTexts: etsysAAAPolicyMIB.setLastUpdated('200407291906Z')
if mibBuilder.loadTexts: etsysAAAPolicyMIB.setOrganization('Enterasys Networks, Inc')
class AAAProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("any", 1), ("none", 2), ("radius", 3), ("tacacs", 4))

etsysAAAPolicyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1))
etsysAAAPolicyMgmtAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1))
etsysAAAMgmtAccessTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1, 1), )
if mibBuilder.loadTexts: etsysAAAMgmtAccessTable.setStatus('current')
etsysAAAMgmtAccessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1, 1, 1), ).setIndexNames((0, "ENTERASYS-AAA-POLICY-MIB", "etsysAAAMgmtAccessProtocol"))
if mibBuilder.loadTexts: etsysAAAMgmtAccessEntry.setStatus('current')
etsysAAAMgmtAccessProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("allProtocols", 1))))
if mibBuilder.loadTexts: etsysAAAMgmtAccessProtocol.setStatus('current')
etsysAAAMgmtRemoteAuthProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1, 1, 1, 2), AAAProtocol().clone('any')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysAAAMgmtRemoteAuthProtocol.setStatus('current')
etsysAAAMgmtRemoteAcctProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1, 1, 1, 3), AAAProtocol().clone('any')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysAAAMgmtRemoteAcctProtocol.setStatus('current')
etsysAAAPolicyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 2))
etsysAAAPolicyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 2, 1))
etsysAAAPolicyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 2, 2))
etsysAAAPolicyMgmtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 2, 2, 1)).setObjects(("ENTERASYS-AAA-POLICY-MIB", "etsysAAAMgmtRemoteAuthProtocol"), ("ENTERASYS-AAA-POLICY-MIB", "etsysAAAMgmtRemoteAcctProtocol"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysAAAPolicyMgmtGroup = etsysAAAPolicyMgmtGroup.setStatus('current')
etsysAAAPolicyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 2, 1, 1)).setObjects(("ENTERASYS-AAA-POLICY-MIB", "etsysAAAPolicyMgmtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysAAAPolicyMIBCompliance = etsysAAAPolicyMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-AAA-POLICY-MIB", etsysAAAPolicyMIBGroups=etsysAAAPolicyMIBGroups, etsysAAAPolicyObjects=etsysAAAPolicyObjects, etsysAAAPolicyMIB=etsysAAAPolicyMIB, etsysAAAMgmtAccessProtocol=etsysAAAMgmtAccessProtocol, etsysAAAPolicyMgmtGroup=etsysAAAPolicyMgmtGroup, etsysAAAMgmtAccessTable=etsysAAAMgmtAccessTable, etsysAAAPolicyMIBCompliances=etsysAAAPolicyMIBCompliances, etsysAAAPolicyMgmtAccess=etsysAAAPolicyMgmtAccess, etsysAAAMgmtRemoteAuthProtocol=etsysAAAMgmtRemoteAuthProtocol, etsysAAAPolicyMIBConformance=etsysAAAPolicyMIBConformance, etsysAAAPolicyMIBCompliance=etsysAAAPolicyMIBCompliance, etsysAAAMgmtRemoteAcctProtocol=etsysAAAMgmtRemoteAcctProtocol, etsysAAAMgmtAccessEntry=etsysAAAMgmtAccessEntry, PYSNMP_MODULE_ID=etsysAAAPolicyMIB, AAAProtocol=AAAProtocol)
