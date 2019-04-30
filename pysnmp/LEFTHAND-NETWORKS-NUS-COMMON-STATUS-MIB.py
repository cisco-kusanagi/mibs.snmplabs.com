#
# PySNMP MIB module LEFTHAND-NETWORKS-NUS-COMMON-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LEFTHAND-NETWORKS-NUS-COMMON-STATUS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:55:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
lhnModules, = mibBuilder.importSymbols("LEFTHAND-NETWORKS-GLOBAL-REG", "lhnModules")
lhnNusCommonStatus, = mibBuilder.importSymbols("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, ObjectIdentity, ModuleIdentity, Integer32, IpAddress, TimeTicks, Bits, MibIdentifier, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "Integer32", "IpAddress", "TimeTicks", "Bits", "MibIdentifier", "iso", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lhnNusCommonStatusModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9804, 1, 1, 99))
if mibBuilder.loadTexts: lhnNusCommonStatusModule.setLastUpdated('0106010000Z')
if mibBuilder.loadTexts: lhnNusCommonStatusModule.setOrganization('LeftHand Networks, Inc.')
status = MibScalar((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 99, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("online", 1), ("offline", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: status.setStatus('current')
statusMessage = MibScalar((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 99, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusMessage.setStatus('current')
mibBuilder.exportSymbols("LEFTHAND-NETWORKS-NUS-COMMON-STATUS-MIB", PYSNMP_MODULE_ID=lhnNusCommonStatusModule, status=status, lhnNusCommonStatusModule=lhnNusCommonStatusModule, statusMessage=statusMessage)
