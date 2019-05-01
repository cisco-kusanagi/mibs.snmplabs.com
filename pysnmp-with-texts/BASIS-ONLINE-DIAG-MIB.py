#
# PySNMP MIB module BASIS-ONLINE-DIAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BASIS-ONLINE-DIAG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:34:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
axisDiagnostics, = mibBuilder.importSymbols("BASIS-MIB", "axisDiagnostics")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, Counter32, Integer32, Bits, NotificationType, Gauge32, IpAddress, MibIdentifier, ModuleIdentity, Counter64, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "Counter32", "Integer32", "Bits", "NotificationType", "Gauge32", "IpAddress", "MibIdentifier", "ModuleIdentity", "Counter64", "ObjectIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
basisOnlineDiagMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 80))
basisOnlineDiagMIB.setRevisions(('2003-06-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: basisOnlineDiagMIB.setRevisionsDescriptions(('Initial version of the MIB. The content of this MIB was originally available in CISCO-WAN-AXIPOP-MIB defined using SMIv1. The applicable objects from CISCO-WAN-AXIPOP-MIB are defined using SMIv2 in this MIB. Also the descriptions of some of the objects have been modified.',))
if mibBuilder.loadTexts: basisOnlineDiagMIB.setLastUpdated('200306110000Z')
if mibBuilder.loadTexts: basisOnlineDiagMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: basisOnlineDiagMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: basisOnlineDiagMIB.setDescription('This MIB contains information on the online diagnostics in MGX82xx(MGX8250, MGX8220, MGX8230 etc) products.')
onlineDiagnostics = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 6, 3))
diagType = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("post", 1), ("onlinediag", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diagType.setStatus('current')
if mibBuilder.loadTexts: diagType.setDescription('This is used to identify the type of diagnostics. post (1) : Power On Self Test. onlineDiag(2) : Online Diagnostics. When a trap is sent to report diagnostics results this is used as a varbind to indicate the type of diagnostics.')
diagResult = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("passed", 1), ("failed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diagResult.setStatus('current')
if mibBuilder.loadTexts: diagResult.setDescription('This is used to indicate the result of the diagnostics.')
diagTestId = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diagTestId.setStatus('current')
if mibBuilder.loadTexts: diagTestId.setDescription('This is used to indicate the test number of the diagnostics test that failed. The value depends upon the implementation in the each of the MGX82xx product.')
boDiagMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 80, 2))
boDiagMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 1))
boDiagMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 2))
boDiagCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 1, 1)).setObjects(("BASIS-ONLINE-DIAG-MIB", "boDiagGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    boDiagCompliance = boDiagCompliance.setStatus('current')
if mibBuilder.loadTexts: boDiagCompliance.setDescription('The compliance statement for entities which implement the basis online diagnostics MIB.')
boDiagGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 2, 1)).setObjects(("BASIS-ONLINE-DIAG-MIB", "diagType"), ("BASIS-ONLINE-DIAG-MIB", "diagResult"), ("BASIS-ONLINE-DIAG-MIB", "diagTestId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    boDiagGroup = boDiagGroup.setStatus('current')
if mibBuilder.loadTexts: boDiagGroup.setDescription('A collection of objects providing the online diagnostics information.')
mibBuilder.exportSymbols("BASIS-ONLINE-DIAG-MIB", basisOnlineDiagMIB=basisOnlineDiagMIB, boDiagMIBCompliances=boDiagMIBCompliances, diagTestId=diagTestId, boDiagMIBGroups=boDiagMIBGroups, onlineDiagnostics=onlineDiagnostics, boDiagCompliance=boDiagCompliance, diagType=diagType, boDiagGroup=boDiagGroup, boDiagMIBConformance=boDiagMIBConformance, PYSNMP_MODULE_ID=basisOnlineDiagMIB, diagResult=diagResult)
