#
# PySNMP MIB module CXOperatingSystem-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXOperatingSystem-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:33:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
cxOperatingSystem, = mibBuilder.importSymbols("CXProduct-SMI", "cxOperatingSystem")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, ModuleIdentity, Bits, MibIdentifier, Unsigned32, IpAddress, NotificationType, iso, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "Bits", "MibIdentifier", "Unsigned32", "IpAddress", "NotificationType", "iso", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cxOsParameter = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1))
cxOsNbBufs = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 1), Integer32().clone(1200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxOsNbBufs.setStatus('mandatory')
if mibBuilder.loadTexts: cxOsNbBufs.setDescription('Determines the total number of data buffers to be created within the system. System heap memory is reduced as the number of buffers is increased. Range of Values: Depends on amount of installed system DRAM, as well as on requirements made by software during initialization. Cannot be set to a value larger than the one chosen for object cxOsNbSystemMsg. Default Value: 1200')
cxOsBufSize = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 2), Integer32().clone(292)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxOsBufSize.setStatus('mandatory')
if mibBuilder.loadTexts: cxOsBufSize.setDescription('Determines the size in bytes of each data buffer. Range of Values: 1 to 65535 Note: The maximum usable size depends on amount of installed system DRAM, as well as on requirements made by software during initialization. Default Value: 292.')
cxOsNbBufsAvail = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxOsNbBufsAvail.setStatus('mandatory')
if mibBuilder.loadTexts: cxOsNbBufsAvail.setDescription('Displays the number of data buffers that has actually been created. If you want to change the number of buffers you must change cxOsNbBufs. Range of Values: Depends on amount of installed system DRAM, as well as on requirements made by software during initialization.')
cxOsNbBufsFree = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxOsNbBufsFree.setStatus('mandatory')
if mibBuilder.loadTexts: cxOsNbBufsFree.setDescription('Displays the number of data buffers that are currently free within the system. Range of Values: Depends on amount of installed system DRAM, as well as on requirements made by software during initialization.')
cxOsNbSystemMsg = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 16), Integer32().clone(1320)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxOsNbSystemMsg.setStatus('mandatory')
if mibBuilder.loadTexts: cxOsNbSystemMsg.setDescription('Determines the number of message buffers defined in the system. One or more data buffers may be attached to a message buffer. Cannot be set to a value smaller than the value of object cxOsNbBufs. Range of Values: from the total number of buffers in the system to 65535 Default Value: 1320')
cxOsNbSystemMsgFree = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxOsNbSystemMsgFree.setStatus('mandatory')
if mibBuilder.loadTexts: cxOsNbSystemMsgFree.setDescription('Displays the number of message buffers currently free in the system. Range of Values:from the total number of buffers in the system to 65535.')
cxOsOptions = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("data", 1), ("inst", 2), ("data-inst", 3), ("pipeline", 4), ("p-data", 5), ("p-inst", 6), ("p-data-inst", 7), ("none", 8))).clone('p-data-inst')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxOsOptions.setStatus('mandatory')
if mibBuilder.loadTexts: cxOsOptions.setDescription('Used for engineering testing only. Used to control data cache, instruction cache and pipeline features. Default value: p-data-inst')
mibBuilder.exportSymbols("CXOperatingSystem-MIB", cxOsOptions=cxOsOptions, cxOsNbBufs=cxOsNbBufs, cxOsParameter=cxOsParameter, cxOsBufSize=cxOsBufSize, cxOsNbSystemMsg=cxOsNbSystemMsg, cxOsNbBufsAvail=cxOsNbBufsAvail, cxOsNbSystemMsgFree=cxOsNbSystemMsgFree, cxOsNbBufsFree=cxOsNbBufsFree)
