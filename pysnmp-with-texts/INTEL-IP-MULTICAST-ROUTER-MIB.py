#
# PySNMP MIB module INTEL-IP-MULTICAST-ROUTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTEL-IP-MULTICAST-ROUTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:54:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
mib2ext, = mibBuilder.importSymbols("INTEL-GEN-MIB", "mib2ext")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, NotificationType, Counter64, Bits, Unsigned32, MibIdentifier, Integer32, ObjectIdentity, iso, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "NotificationType", "Counter64", "Bits", "Unsigned32", "MibIdentifier", "Integer32", "ObjectIdentity", "iso", "TimeTicks", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ipmrouter = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 32))
conf = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 32, 1))
confMaxDvmrpRoutes = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confMaxDvmrpRoutes.setStatus('mandatory')
if mibBuilder.loadTexts: confMaxDvmrpRoutes.setDescription('Limits the number of DVMRP routes handled by the router')
confIfTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 2), )
if mibBuilder.loadTexts: confIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: confIfTable.setDescription('This table contains configuration information for each IP Multicast link.')
confIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 2, 1), ).setIndexNames((0, "INTEL-IP-MULTICAST-ROUTER-MIB", "confIfIndex"))
if mibBuilder.loadTexts: confIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: confIfEntry.setDescription('Configuration information for the IP Multicast link.')
confIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: confIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: confIfIndex.setDescription('The ifIndex of the IP link.')
confIfMCRouteProto = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confIfMCRouteProto.setStatus('mandatory')
if mibBuilder.loadTexts: confIfMCRouteProto.setDescription('The multicast Routing Protocol used on the link.')
confIfIgmpQueryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confIfIgmpQueryInterval.setStatus('mandatory')
if mibBuilder.loadTexts: confIfIgmpQueryInterval.setDescription('The IGMP query interval used on the link.')
confIfIgmpRobustness = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confIfIgmpRobustness.setStatus('mandatory')
if mibBuilder.loadTexts: confIfIgmpRobustness.setDescription('The IGMP robustness variable used on the link.')
confIfDvmrpMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confIfDvmrpMetric.setStatus('mandatory')
if mibBuilder.loadTexts: confIfDvmrpMetric.setDescription('The DVMRP metric (cost) used on the link.')
confIfDvmrpUnreachableMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confIfDvmrpUnreachableMetric.setStatus('mandatory')
if mibBuilder.loadTexts: confIfDvmrpUnreachableMetric.setDescription('When a route report is received this parameter is used to determine if a route should be considered unreachable and thus ignored ')
confIfCreateObj = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confIfCreateObj.setStatus('mandatory')
if mibBuilder.loadTexts: confIfCreateObj.setDescription('Create a non existing table entry. If the entry already exist, genError is returned. Binary format: 1 bytes confIfMCRouteProto 4 bytes confIfIgmpQueryInterval 4 bytes confIfIgmpRobustness 1 byte confIfDvmrpMetric 1 bytes confIfDvmrpUnreachableMetric ')
confIfDeleteObj = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("delete", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confIfDeleteObj.setStatus('mandatory')
if mibBuilder.loadTexts: confIfDeleteObj.setDescription('Delete an existing table entry')
mibBuilder.exportSymbols("INTEL-IP-MULTICAST-ROUTER-MIB", ipmrouter=ipmrouter, confIfDvmrpMetric=confIfDvmrpMetric, confIfDvmrpUnreachableMetric=confIfDvmrpUnreachableMetric, confIfCreateObj=confIfCreateObj, confIfEntry=confIfEntry, confIfIgmpQueryInterval=confIfIgmpQueryInterval, confIfDeleteObj=confIfDeleteObj, confIfIndex=confIfIndex, confIfMCRouteProto=confIfMCRouteProto, confIfTable=confIfTable, conf=conf, confMaxDvmrpRoutes=confMaxDvmrpRoutes, confIfIgmpRobustness=confIfIgmpRobustness)
