#
# PySNMP MIB module CTRON-DCM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-DCM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:29:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ctDcm, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctDcm")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ObjectIdentity, Gauge32, Counter32, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, Bits, TimeTicks, iso, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "Gauge32", "Counter32", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "Bits", "TimeTicks", "iso", "Unsigned32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dCM = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 6, 1))
dCMMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 6, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dCMMode.setStatus('mandatory')
if mibBuilder.loadTexts: dCMMode.setDescription('A value which indicates whether this module supports a view chassis-wide of management information, accessed via chassis-ip. This MIB view is actually composed of information which is distributed between modules within the chassis but is able to be viewed as a collective whole. When a module is in standalone mode, it only supports original, module-level mibs. In distributed mode, the module will operate in conjunction with other distributed modules to share management information and present it to management clients through the chassis ip. 0 = STANDALONE 1 = DISTRIBUTED ')
mibBuilder.exportSymbols("CTRON-DCM-MIB", dCM=dCM, dCMMode=dCMMode)
