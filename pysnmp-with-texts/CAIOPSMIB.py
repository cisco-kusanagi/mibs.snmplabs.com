#
# PySNMP MIB module CAIOPSMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CAIOPSMIB
# Produced by pysmi-0.3.4 at Wed May  1 11:46:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
caiSysMgt, = mibBuilder.importSymbols("CAIMIB", "caiSysMgt")
cai, = mibBuilder.importSymbols("CAISECMIB", "cai")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ObjectIdentity, MibIdentifier, Integer32, Gauge32, NotificationType, NotificationType, ModuleIdentity, enterprises, Counter32, IpAddress, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Integer32", "Gauge32", "NotificationType", "NotificationType", "ModuleIdentity", "enterprises", "Counter32", "IpAddress", "iso", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
caiOps = MibIdentifier((1, 3, 6, 1, 4, 1, 791, 2, 4))
caiOpsLstMsg = MibScalar((1, 3, 6, 1, 4, 1, 791, 2, 4, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: caiOpsLstMsg.setStatus('mandatory')
if mibBuilder.loadTexts: caiOpsLstMsg.setDescription('This object type is used when defining TRAPs to send Security messages in a trap. ')
caiOpsT1 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,2000)).setObjects(("CAIOPSMIB", "caiOpsLstMsg"))
if mibBuilder.loadTexts: caiOpsT1.setDescription('Reason: A dataset violation occurred Action: Msgref: ACF99913 ')
caiOpsT2 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,2001)).setObjects(("CAIOPSMIB", "caiOpsLstMsg"))
if mibBuilder.loadTexts: caiOpsT2.setDescription('Reason: A resource violation occurred Action: Msgref: ACF04056 ')
mibBuilder.exportSymbols("CAIOPSMIB", caiOps=caiOps, caiOpsT2=caiOpsT2, caiOpsT1=caiOpsT1, caiOpsLstMsg=caiOpsLstMsg)
