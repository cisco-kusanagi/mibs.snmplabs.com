#
# PySNMP MIB module CAIOPSMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CAIOPSMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:29:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
caiSysMgt, = mibBuilder.importSymbols("CAIMIB", "caiSysMgt")
cai, = mibBuilder.importSymbols("CAISECMIB", "cai")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, ModuleIdentity, Bits, IpAddress, enterprises, Counter64, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, Integer32, ObjectIdentity, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "ModuleIdentity", "Bits", "IpAddress", "enterprises", "Counter64", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "Integer32", "ObjectIdentity", "Counter32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
caiOps = MibIdentifier((1, 3, 6, 1, 4, 1, 791, 2, 4))
caiOpsLstMsg = MibScalar((1, 3, 6, 1, 4, 1, 791, 2, 4, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: caiOpsLstMsg.setStatus('mandatory')
caiOpsT1 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,2000)).setObjects(("CAIOPSMIB", "caiOpsLstMsg"))
caiOpsT2 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,2001)).setObjects(("CAIOPSMIB", "caiOpsLstMsg"))
mibBuilder.exportSymbols("CAIOPSMIB", caiOps=caiOps, caiOpsT2=caiOpsT2, caiOpsLstMsg=caiOpsLstMsg, caiOpsT1=caiOpsT1)
