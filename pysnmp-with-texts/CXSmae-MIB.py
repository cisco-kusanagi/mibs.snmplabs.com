#
# PySNMP MIB module CXSmae-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXSmae-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:33:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
cxSystemManagement, = mibBuilder.importSymbols("CXProduct-SMI", "cxSystemManagement")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, TimeTicks, Bits, IpAddress, Counter32, Unsigned32, Gauge32, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Bits", "IpAddress", "Counter32", "Unsigned32", "Gauge32", "Integer32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cxSmRestart = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 13, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("system-idle", 0), ("warm-start-save-end", 1), ("cold-start", 2), ("warm-start-without-save", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxSmRestart.setStatus('mandatory')
if mibBuilder.loadTexts: cxSmRestart.setDescription('Determines the reset method used throughout the system. The setting of this object is dynamic. The system immediately implements the option you enter. Options: warm-start (0): system is idling no action is taken. warm-start (1): this value is not taking effect immediatelly. When the user sets this object to 1 the system waits till it finishes saving the configuration before it tkes the value then it restarts. cold-start (2): system reset to factory defaults warm-start-without-save (3): system reset to previous configuration - no save Default Value: none Configuration Changed: operative')
cxSmConfig = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 13, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("save", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: cxSmConfig.setStatus('mandatory')
if mibBuilder.loadTexts: cxSmConfig.setDescription('Determines the save method used throughout the system. The setting of this object is dynamic. The system immediately implements the option you enter. Options: save (1): saves the current configuration into flash memory. This configuraton will be used in the next warm start. Default Value: none Configuration Changed: operative ')
mibBuilder.exportSymbols("CXSmae-MIB", cxSmConfig=cxSmConfig, cxSmRestart=cxSmRestart)
