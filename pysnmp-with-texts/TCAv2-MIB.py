#
# PySNMP MIB module TCAv2-MIB (http://pysnmp.sf.net)
# Produced by pysmi-0.0.1 from TCAv2-MIB at Fri May  8 14:29:57 2015
# On host cray platform Linux version 2.6.37.6-smp by user tt
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, enterprises, iso, Gauge32, MibIdentifier, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "enterprises", "iso", "Gauge32", "MibIdentifier", "Bits", "Counter32")
( DisplayString, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp")
bellcore = MibIdentifier(enterprises.getName() + (148,))
requirements = MibIdentifier(bellcore.getName() + (1,))
tcaMIB = MibIdentifier(requirements.getName() + (5,))
tcaObjects = MibIdentifier(tcaMIB.getName() + (1,))
tcaTable = MibTable(tcaObjects.getName() + (1,), )
if mibBuilder.loadTexts: tcaTable.setDescription('The Threshold Crossing Alert table.')
tcaEntry = MibTableRow(tcaTable.getName() + (1,), ).setIndexNames((0, "TCAv2-MIB", "tcaIfIndex"), (0, "TCAv2-MIB", "tcaIndex"))
if mibBuilder.loadTexts: tcaEntry.setDescription('An entry in the Threshold Crossing Alert table.')
tcaIfIndex = MibTableColumn(tcaEntry.getName() + (1,), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648,2147483647)))
if mibBuilder.loadTexts: tcaIfIndex.setDescription("The value of this object is equal to MIB II's\n                      ifIndex value for this interface sublayer\n                      (ifEntry).")
tcaIndex = MibTableColumn(tcaEntry.getName() + (2,), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648,2147483647)))
if mibBuilder.loadTexts: tcaIndex.setDescription('The value of this object is used as one of the\n                      indices for this table.  It is a unique identifier\n                      for this row in the table for this interface\n                      (ifIndex).  The value of this object can be from 1\n                      to N, where N is the number of potential TCAs for\n                      this interface sublayer (ifEntry).')
tcaObject = MibTableColumn(tcaEntry.getName() + (3,), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcaObject.setDescription('The value of this object is the OBJECT IDENTIFIER\n                      of the counter object being thresholded.  The\n                      counter objects being thresholded are defined in\n                      other MIB Modules.')
tcaObjectDesc = MibTableColumn(tcaEntry.getName() + (4,), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcaObjectDesc.setDescription('The value of this object is a description of the\n                      counter object being thresholded.  For example,\n                      DS1 Coding Violations.')
tcaThreshold = MibTableColumn(tcaEntry.getName() + (5,), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648,2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcaThreshold.setDescription('The value of this object is the threshold value\n                      of the counter object being thresholded.')
tcaSampleType = MibTableColumn(tcaEntry.getName() + (6,), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8,)).clone(namedValues=NamedValues(("intervalAbsoluteValue", 1), ("intervalDeltaValue", 2), ("intervalFallingAlarm", 3), ("intervalRisingAlarm", 4), ("intervalAtValueAlarm", 5), ("intervalNotAtValueAlarm", 6), ("intervalIncludesValue", 7), ("intervalIncludesNotValue", 8),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcaSampleType.setDescription('The value of this object is the sample type of\n                      the object being thresholded from the\n                      perspective of the CNM or XA-OM customer.\n                      This object can be used for the following\n                      data types:\n                      (a) Counters\n                      (b) Counters measured over certain intervals,\n                          where the Counters are reset to zero at the end\n                          of the interval and as a result have the\n                          syntax Gauge.\n                      (c) Gauges (other than (b))\n                      (d) (Enumerated) INTEGER\n                      (e) (Enumerated) INTEGER that is used as a bitmap.\n                      The enumerated values of this object apply to\n                      these data types as follows:\n\n                                          |        possible values        |\n                          data type       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |\n                      --------------------+---+---+---+---+---+---+---+---+\n                      (a) Counter         |   | X |   |   |   |   |   |   |\n                      (b) IntervalCounter | X |   |   |   |   |   |   |   |\n                      (c) Gauge           |   |   | X | X |   |   |   |   |\n                      (d) Enum INT        |   |   |   |   | X | X |   |   |\n                      (e) Enum INT(bitmap)|   |   |   |   |   |   | X | X |\n                      --------------------+---+---+---+---+---+---+---+---+\n\n                      (a) Counter values can only rise. An\n\n\n\n\n\n\n\n                          alarm may be triggered when the value has\n                          risen a delta amount within a sample period.\n                      (b) IntervalCounter values can only rise within an\n                          interval and are reset at the end of the\n                          interval. An alarm may be triggered when\n                          the value has exceeded an absolute value.\n                      (c) A Gauge value may rise and fall. An alarm\n                          may be triggered when the value has risen or\n                          fallen a certain amount.\n                      (d) An INTEGER may assume values in any sequence.\n                          An alarm may be triggered when the value\n                          does equal or doesnot equal a certain\n                          specified value.\n                      (e) A bitmap may assume values that represent\n                          one or more bits to be set. An alarm may be\n                          triggered when the value does include or not\n                          include the combined value of certain bits.\n                          Note that for (c), (d), and (e) only one alarm\n                          needs to be generated, i.e., at first detection\n                          of this event.')
tcaCounts = MibTableColumn(tcaEntry.getName() + (7,), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcaCounts.setDescription('The value of this object is the number of times\n                      the threshold was crossed for this counter object,\n                      since sysUpTime was initialized or restarted.\n                      This counter is a continuous counter.  It should\n                      be noted that as this object has a SYNTAX of\n                      Counter, that it does not have a defined initial\n                      value.  However, it is recommended that this\n                      object be initialized to zero.')
tcaTimeStamp = MibTableColumn(tcaEntry.getName() + (8,), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcaTimeStamp.setDescription("The value of this object is equal to the value of\n                      MIB-II's sysUpTime object at which last (latest)\n                      threshold was crossed for this counter object.\n\n\n\n\n\n\n\n                      The value of this object is set to zero at\n                      (re)initialization.")
tcaTrapEnabler = MibTableColumn(tcaEntry.getName() + (9,), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2,)).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2),))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tcaTrapEnabler.setDescription("Indicates whether fyiTraps should be generated\n                      for this threshold crossing count (tcaObject).\n                      The physical layer counters' and gauges' (e.g.,\n                      DS1, DS3, SONET, and PLCP) TCAs should have a\n                      default value of disabled(2).  The SMDS service\n                      violations and higher layer protocol violations\n                      counters' TCAs should have a default value of\n                      enabled(1).  A fyiTrap, when generated, shall have\n                      the following varBind list: tcaObject,\n                      tcaObjectDesc, tcaThreshold, and tcaTimeStamp.")
tcaConformance = MibIdentifier(tcaMIB.getName() + (2,))
tcaGroups = MibIdentifier(tcaConformance.getName() + (1,))
tcaCompliances = MibIdentifier(tcaConformance.getName() + (2,))
tcaCompliance = MibIdentifier(tcaCompliances.getName() + (1,))
tcaGroup = MibIdentifier(tcaGroups.getName() + (1,))
mibBuilder.exportSymbols("TCAv2-MIB", tcaMIB=tcaMIB, tcaEntry=tcaEntry, tcaObjectDesc=tcaObjectDesc, tcaCompliances=tcaCompliances, tcaTable=tcaTable, tcaTrapEnabler=tcaTrapEnabler, tcaThreshold=tcaThreshold, tcaCounts=tcaCounts, tcaIndex=tcaIndex, tcaCompliance=tcaCompliance, tcaGroups=tcaGroups, requirements=requirements, tcaSampleType=tcaSampleType, tcaGroup=tcaGroup, bellcore=bellcore, tcaIfIndex=tcaIfIndex, tcaObject=tcaObject, tcaObjects=tcaObjects, tcaTimeStamp=tcaTimeStamp, tcaConformance=tcaConformance)