#
# PySNMP MIB module IPFIX-SELECTOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPFIX-SELECTOR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:44:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, ModuleIdentity, Counter64, Gauge32, MibIdentifier, Integer32, IpAddress, mib_2, Counter32, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "ModuleIdentity", "Counter64", "Gauge32", "MibIdentifier", "Integer32", "IpAddress", "mib-2", "Counter32", "iso", "NotificationType")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
ipfixSelectorMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 194))
ipfixSelectorMIB.setRevisions(('2012-06-11 00:00', '2010-03-15 00:00',))
if mibBuilder.loadTexts: ipfixSelectorMIB.setLastUpdated('201206110000Z')
if mibBuilder.loadTexts: ipfixSelectorMIB.setOrganization('IETF IPFIX Working Group')
ipfixSelectorObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 1))
ipfixSelectorConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 2))
ipfixSelectorFunctions = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 1, 1))
ipfixFuncSelectAll = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 1, 1, 1))
ipfixFuncSelectAllAvail = MibScalar((1, 3, 6, 1, 2, 1, 194, 1, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixFuncSelectAllAvail.setStatus('current')
ipfixSelectorCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 2, 1))
ipfixSelectorGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 2, 2))
ipfixSelectorBasicCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 194, 2, 1, 1)).setObjects(("IPFIX-SELECTOR-MIB", "ipfixSelectorBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipfixSelectorBasicCompliance = ipfixSelectorBasicCompliance.setStatus('current')
ipfixSelectorBasicGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 194, 2, 2, 1)).setObjects(("IPFIX-SELECTOR-MIB", "ipfixFuncSelectAllAvail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipfixSelectorBasicGroup = ipfixSelectorBasicGroup.setStatus('current')
mibBuilder.exportSymbols("IPFIX-SELECTOR-MIB", ipfixFuncSelectAllAvail=ipfixFuncSelectAllAvail, ipfixSelectorBasicCompliance=ipfixSelectorBasicCompliance, ipfixSelectorGroups=ipfixSelectorGroups, ipfixSelectorConformance=ipfixSelectorConformance, PYSNMP_MODULE_ID=ipfixSelectorMIB, ipfixSelectorObjects=ipfixSelectorObjects, ipfixFuncSelectAll=ipfixFuncSelectAll, ipfixSelectorCompliances=ipfixSelectorCompliances, ipfixSelectorMIB=ipfixSelectorMIB, ipfixSelectorBasicGroup=ipfixSelectorBasicGroup, ipfixSelectorFunctions=ipfixSelectorFunctions)
