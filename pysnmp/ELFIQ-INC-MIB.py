#
# PySNMP MIB module ELFIQ-INC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELFIQ-INC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:45:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, Counter64, TimeTicks, IpAddress, MibIdentifier, enterprises, ObjectIdentity, Counter32, iso, Gauge32, Integer32, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "Counter64", "TimeTicks", "IpAddress", "MibIdentifier", "enterprises", "ObjectIdentity", "Counter32", "iso", "Gauge32", "Integer32", "NotificationType", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
elfiqInc = ModuleIdentity((1, 3, 6, 1, 4, 1, 19713))
if mibBuilder.loadTexts: elfiqInc.setLastUpdated('200811190000Z')
if mibBuilder.loadTexts: elfiqInc.setOrganization('Elfiq Inc.')
elfiqMIBProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 19713, 1))
elfiqMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 19713, 2))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 19713, 1, 1))
linkBalancer = MibIdentifier((1, 3, 6, 1, 4, 1, 19713, 1, 2))
commonConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 19713, 2, 1))
linkBalancerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 19713, 2, 2))
mibBuilder.exportSymbols("ELFIQ-INC-MIB", PYSNMP_MODULE_ID=elfiqInc, elfiqInc=elfiqInc, elfiqMIBConformance=elfiqMIBConformance, linkBalancer=linkBalancer, common=common, commonConformance=commonConformance, linkBalancerConformance=linkBalancerConformance, elfiqMIBProducts=elfiqMIBProducts)
