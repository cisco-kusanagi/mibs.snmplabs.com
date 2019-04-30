#
# PySNMP MIB module TPLINK-CLUSTERMANAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-CLUSTERMANAGE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:16:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, Counter64, Gauge32, NotificationType, IpAddress, Integer32, iso, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "Counter64", "Gauge32", "NotificationType", "IpAddress", "Integer32", "iso", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
clusterManage, = mibBuilder.importSymbols("TPLINK-CLUSTER-MIB", "clusterManage")
clusterRole = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("commander", 0), ("member", 1), ("candidate", 2), ("individual", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clusterRole.setStatus('current')
mibBuilder.exportSymbols("TPLINK-CLUSTERMANAGE-MIB", clusterRole=clusterRole)
