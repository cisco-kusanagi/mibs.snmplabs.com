#
# PySNMP MIB module BSU-BRGCLUSTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BSU-BRGCLUSTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:41:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
bsu, = mibBuilder.importSymbols("ANIROOT-MIB", "bsu")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, IpAddress, MibIdentifier, TimeTicks, Counter64, Bits, Integer32, NotificationType, Gauge32, ObjectIdentity, ModuleIdentity, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "MibIdentifier", "TimeTicks", "Counter64", "Bits", "Integer32", "NotificationType", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aniBsuBridge = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 3, 5))
if mibBuilder.loadTexts: aniBsuBridge.setLastUpdated('0209251530Z')
if mibBuilder.loadTexts: aniBsuBridge.setOrganization('Aperto Networks')
if mibBuilder.loadTexts: aniBsuBridge.setContactInfo(' Postal: Aperto Networks Inc 1637 S Main Street Milpitas, California 95035 Tel: +1 408 719 9977 ')
if mibBuilder.loadTexts: aniBsuBridge.setDescription('This group allows Configuration/Viewing of Bridging and Clustering parameters for BSU. Clusters can be added and deleted using Configuration Manager and viewed using SNMP. When BSU is running in point to point mode, this group is not applicable. Also for PacketWave 750 this group is not applicable. ')
aniBsuSuBridgeEnable = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("not-applicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuSuBridgeEnable.setStatus('current')
if mibBuilder.loadTexts: aniBsuSuBridgeEnable.setDescription('This parameter is used to enable/disable SU to SU bridging on BSU wireless ports. When BSU is running in point to point mode, this object is not-applicable. Also for PacketWave 750, this group is not-applicable. ')
mibBuilder.exportSymbols("BSU-BRGCLUSTER-MIB", PYSNMP_MODULE_ID=aniBsuBridge, aniBsuSuBridgeEnable=aniBsuSuBridgeEnable, aniBsuBridge=aniBsuBridge)
