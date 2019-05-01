#
# PySNMP MIB module LEFTHAND-NETWORKS-NUS-COMMON-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LEFTHAND-NETWORKS-NUS-COMMON-STATUS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:06:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
lhnModules, = mibBuilder.importSymbols("LEFTHAND-NETWORKS-GLOBAL-REG", "lhnModules")
lhnNusCommonStatus, = mibBuilder.importSymbols("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ModuleIdentity, NotificationType, Bits, iso, Unsigned32, Counter64, IpAddress, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "NotificationType", "Bits", "iso", "Unsigned32", "Counter64", "IpAddress", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lhnNusCommonStatusModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9804, 1, 1, 99))
if mibBuilder.loadTexts: lhnNusCommonStatusModule.setLastUpdated('0106010000Z')
if mibBuilder.loadTexts: lhnNusCommonStatusModule.setOrganization('LeftHand Networks, Inc.')
if mibBuilder.loadTexts: lhnNusCommonStatusModule.setContactInfo(' Author: Jose Faria LeftHand Networks postal: 6185 Arapahoe Rd. Boulder, CO 80301 USA email: jfaria@lefthandnetworks.com phone: +1 303 449-4100 ')
if mibBuilder.loadTexts: lhnNusCommonStatusModule.setDescription('Status items for NUS Devices')
status = MibScalar((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 99, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("online", 1), ("offline", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: status.setStatus('current')
if mibBuilder.loadTexts: status.setDescription('LeftHand Networks MIB status')
statusMessage = MibScalar((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 99, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusMessage.setStatus('current')
if mibBuilder.loadTexts: statusMessage.setDescription('LeftHand Networks MIB status message')
mibBuilder.exportSymbols("LEFTHAND-NETWORKS-NUS-COMMON-STATUS-MIB", lhnNusCommonStatusModule=lhnNusCommonStatusModule, status=status, PYSNMP_MODULE_ID=lhnNusCommonStatusModule, statusMessage=statusMessage)
