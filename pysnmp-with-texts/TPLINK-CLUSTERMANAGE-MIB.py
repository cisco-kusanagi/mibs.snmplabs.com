#
# PySNMP MIB module TPLINK-CLUSTERMANAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-CLUSTERMANAGE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:24:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, Bits, MibIdentifier, Gauge32, NotificationType, Integer32, Counter32, ModuleIdentity, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Bits", "MibIdentifier", "Gauge32", "NotificationType", "Integer32", "Counter32", "ModuleIdentity", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
clusterManage, = mibBuilder.importSymbols("TPLINK-CLUSTER-MIB", "clusterManage")
clusterRole = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("commander", 0), ("member", 1), ("candidate", 2), ("individual", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clusterRole.setStatus('current')
if mibBuilder.loadTexts: clusterRole.setDescription('This object indicates the current role of the switch. You can not set the role to commander with this object. You can set the role to candidate when the role is commander. You can set the role to individual when the role is candidate or member. You can set the role to candidate when the role is individual.')
mibBuilder.exportSymbols("TPLINK-CLUSTERMANAGE-MIB", clusterRole=clusterRole)
